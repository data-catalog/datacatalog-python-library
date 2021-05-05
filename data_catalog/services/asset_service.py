from typing import List, Union, Dict, Optional
import pandas as pd

from data_catalog import config_provider
from data_catalog.models.asset import Asset

from data_catalog.client.asset import ApiClient as AssetApiClient, ApiException as AssetApiException
from data_catalog.client.user import ApiClient as UserApiClient
from data_catalog.client.asset.api import AssetApi
from data_catalog.client.user import UserLoginRequest, UserLoginResponse
from data_catalog.client.user import AuthenticationApi, ApiException as UserApiException


class AssetService:
    """
    A client to interact with the Asset service.
    This client provides operations to list and find services.
    """

    def __init__(self, username: str = None, password: str = None, api_key: str = None):
        """
        Constructor of the Asset Service.
        The configuration will be loaded from config.yaml.

        :param str username: Optional parameter for username and password authentication.
        :param str password: Optional parameter for username and password authentication.
        :param str api_key: Optional parameter for API key authentication. (Recommended)
        """

        # Create an instance of the API Client
        self.api_client = AssetApiClient(configuration=config_provider.get_asset_service_config())
        # Create an instance of the API class
        self.asset_api = AssetApi(self.api_client)

        if username is not None and password is not None:
            token: str = self._get_access_token(username, password)

            self.api_client.configuration.access_token = token
            config_provider.set_access_token(token)
        elif api_key is not None:
            self.api_client.configuration.access_token = api_key
            config_provider.set_access_token(api_key)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.api_client.close()

    def _get_access_token(self, username: str, password: str):
        user_login_request = UserLoginRequest(
            username, password,
            local_vars_configuration=self.api_client.configuration
        )

        with UserApiClient(configuration=config_provider.get_user_service_config()) as user_api_client:
            auth_api = AuthenticationApi(user_api_client)
            try:
                user_login_response: UserLoginResponse = auth_api.login(user_login_request=user_login_request)
            except UserApiException:
                raise PermissionError('Username or password is incorrect.')

        return user_login_response.token

    def list_assets(self, search_term: str = None, output_format: str = 'list') \
            -> Union[List[Asset], Dict[str, Asset], pd.DataFrame]:
        """
        Returns a list of all the assets available.
        If search_term is provided, only assets which match the search_term will be returned.

        :param str search_term: Optional. Filters services which match the search_term.

        :param str output_format: Specifies the format of the output.
                                  - If 'list the output is a list of assets
                                  - If 'dict' the output is a dict of assets
                                  - If 'dataframe' the output is a pandas DataFrame

        :return: All available assets which match the filter criteria(if specified).
                 If the output_format is 'list': returns a list of assets.
                 If the output_format is 'dict': returns a mapping from id to asset as a dictionary.
                 If the output_format is 'dataframe': returns a pandas DataFrame, where each row represents an asset,
                                                      the indexes are the ids, and the columns represent the attributes
                                                      of the asset.
        :rtype: list[Asset] | dict[str, Asset] | pd.DataFrame
        """

        asset_responses = self.asset_api.search_assets(keyword=search_term) if search_term is not None \
            else self.asset_api.get_assets()

        asset_generator = (Asset.from_response(asset) for asset in asset_responses)

        if output_format == 'list':
            return list(asset_generator)
        elif output_format == 'dict':
            return {asset.id: asset for asset in asset_generator}
        elif output_format == 'dataframe':
            return pd.DataFrame((asset.to_dict() for asset in asset_generator)).set_index('id')
        else:
            raise ValueError('Invalid output format specified.')

    def get_asset(self, asset_id: str) -> Optional[Asset]:
        """
        Returns the asset with the id of asset_id.

        :param str asset_id: The id of the asset to return
        :return: Returns the asset with id of asset_id if found, otherwise return None.
        :rtype: Asset | None
        """
        try:
            asset_response = self.asset_api.get_asset(asset_id)
        except AssetApiException as err:
            if err.status == 404:
                return None
            else:
                raise err

        return Asset.from_response(asset_response)
