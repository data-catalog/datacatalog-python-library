from typing import List

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

    def list_assets(self) -> List[Asset]:
        """
        Returns a list of all the assets available.

        :return: All available assets
        :rtype: list[Asset]
        """

        return [Asset.from_response(asset) for asset in self.asset_api.get_assets()]

    def get_asset(self, asset_id: str) -> Asset:
        """
        Returns the asset with the id of asset_id.

        :param str asset_id: The id of the asset to return
        :return: Returns the asset with id of asset_id if found, otherwise return None.
        :rtype: Asset | None
        """

        return Asset.from_response(self.asset_api.get_asset(asset_id))
