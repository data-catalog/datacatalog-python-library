from typing import List, Union, Dict

import pandas as pd

from data_catalog.assets import Asset
from data_catalog.client.asset import ApiClient, Configuration
from data_catalog.client.asset.api import AssetApi


class AssetService:
    """
    A client to interact with the Asset service.
    This client provides operations to list and find assets.
    """

    def __init__(self, configuration: Configuration = None):
        """
        Constructor of the Asset Service.

        :param Configuration configuration: Configuration for the service, which may include user credentials
                                            or server endpoint.
                                            If not set, the default configuration will be used.
        """

        # Create an instance of the API Client
        self.api_client = ApiClient(configuration=configuration)

        # Create an instance of the API class
        self.asset_api = AssetApi(self.api_client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.api_client is not None:
            self.api_client.close()

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
