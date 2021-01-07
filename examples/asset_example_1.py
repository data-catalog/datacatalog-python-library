from data_catalog.assets import AssetService
from data_catalog.client.asset import Configuration, ApiClient, Location, Parameter, AssetCreationRequest
import data_catalog.assets as assets


with AssetService(username="dzsotti99", password="kecske") as asset_service:
    # l = assets.list_assets(api_client)
    # print(l)
    # asset = assets.get_asset(api_client, '1')
    # print(type(asset))
    location = Location(type="url", parameters=[Parameter(key="url", value="http://ssss.com")])
    asset_request = AssetCreationRequest(name="frompython", description="asd", format="csv", location=location, tags=[])
    asset_service.asset_api.create_asset(asset_creation_request=asset_request)

    # asset1 = assets.Asset('222', format='csv', location=Location('url', parameters=[Parameter('url', 'https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-June-2020-quarter/Download-data/business-price-indexes-june-2020-quarter-corrections-to-previously-published-statistics.csv')]))
    # print(asset1.get_data())
