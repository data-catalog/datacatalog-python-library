from data_catalog.assets import AssetService
from data_catalog.client.asset import Configuration, ApiClient, Location, Parameter, AssetCreationRequest
import data_catalog.assets as assets


with AssetService(username="dzsotti99", password="kecske") as asset_service:
    location = Location(type="url", parameters=[Parameter(key="url", value="http://ssss.com")])
    asset_request = AssetCreationRequest(name="frompython", description="asd", format="csv", location=location, tags=[])
    asset_service.asset_api.create_asset(asset_creation_request=asset_request)

