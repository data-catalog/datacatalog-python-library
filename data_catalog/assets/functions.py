from typing import List

from data_catalog.assets import Asset
from data_catalog.client import ApiClient
from data_catalog.client.api import AssetApi


def list_assets(api_client: ApiClient) -> List[Asset]:
    # Create an instance of the API class
    asset_api = AssetApi(api_client)

    return [Asset.from_response(asset) for asset in asset_api.get_assets()]


def get_asset(api_client: ApiClient, asset_id: str) -> Asset:
    asset_api = AssetApi(api_client)
    return Asset.from_response(asset_api.get_asset(asset_id))

