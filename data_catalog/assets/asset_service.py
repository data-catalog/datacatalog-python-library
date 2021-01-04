from typing import List, Union, Dict

import pandas as pd

from data_catalog import configloader
from data_catalog.assets import Asset
from data_catalog.client.asset import ApiClient as AssetApiClient
from data_catalog.client.user import ApiClient as UserApiClient
from data_catalog.client.asset.api import AssetApi
from data_catalog.client.user import UserApi, UserLoginRequest, UserLoginResponse, ApiException


class AssetService:
    """
    A client to interact with the Asset service.
    This client provides operations to list and find assets.
    """

    def __init__(self, username: str = None, password: str = None):
        """
        Constructor of the Asset Service.
        The configuration will be loaded from config.yaml.
        """

        # Create an instance of the API Client
        self.api_client = AssetApiClient(configuration=configloader.load_asset_service_config())
        # Create an instance of the API class
        self.asset_api = AssetApi(self.api_client)

        if username is not None and password is not None:
            token: str = self._get_access_token(username, password)
            print(token)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.api_client is not None:
            self.api_client.close()

    def _get_access_token(self, username: str, password: str):
        user_login_request = UserLoginRequest(
            username, password,
            local_vars_configuration=self.api_client.configuration
        )

        with UserApiClient(configuration=configloader.load_user_service_config()) as user_api_client:
            user_api = UserApi(user_api_client)
            try:
                user_login_response: UserLoginResponse = user_api.login(user_login_request=user_login_request)
            except ApiException:
                raise PermissionError('Username or password is incorrect.')

        return user_login_response.token

    def list_assets(self, namespace: str = None, tags: List[str] = None, output_format: str = 'list') \
            -> Union[List[Asset], Dict[str, Asset], pd.DataFrame]:
        """
        Returns a list of all the assets available.

        :param str namespace: Optional. Filters assets which have the specified namespace.
        :param list[str] tags: Optional. Filters assets which have at least one of the specified tags.
        :param str output_format: Specifies the format of the output.
                                  - If 'list the output is a list of assets
                                  - If 'dict' the output is a dict of assets
                                  - If 'dataframe' the output is a pandas DataFrame

        :return: All available assets which match the filter criteria(namespace, tags).
                 If the output_format is 'list': returns a list of assets.
                 If the output_format is 'dict': returns a mapping from id to asset as a dictionary.
                 If the output_format is 'dataframe': returns a pandas DataFrame, where each row represents an asset,
                                                      the indexes are the ids, and the columns represent the attributes
                                                      of the asset.
        :rtype: list[Asset] | dict[str, Asset] | pd.DataFrame
        """
        asset_responses = self.asset_api.get_assets(namespace=namespace, tags=tags)
        asset_generator = (Asset.from_response(asset) for asset in asset_responses)

        if output_format == 'list':
            return list(asset_generator)
        elif output_format == 'dict':
            return {asset.id: asset for asset in asset_generator}
        elif output_format == 'dataframe':
            return pd.DataFrame((asset.to_dict() for asset in asset_generator)).set_index('id')
        else:
            raise NotImplementedError

    def get_asset(self, asset_id: str) -> Asset:
        """
        Returns the asset with the id of asset_id.

        :param str asset_id: The id of the asset to return
        :return: Returns the asset with id of asset_id if found, otherwise return None.
        :rtype: Asset | None
        """

        return Asset.from_response(self.asset_api.get_asset(asset_id))
