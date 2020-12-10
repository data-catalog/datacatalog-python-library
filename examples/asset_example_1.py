from data_catalog.assets import AssetService
from data_catalog.client.asset import Configuration, ApiClient, Location, Parameter
import data_catalog.assets as assets


configuration = Configuration(
    host="http://localhost:3100"
)

with AssetService(configuration=configuration) as asset_service:
    # l = assets.list_assets(api_client)
    # print(l)
    # asset = assets.get_asset(api_client, '1')
    # print(type(asset))

    asset1 = assets.Asset('222', format='csv', location=Location('url', parameters=[Parameter('url', 'https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-June-2020-quarter/Download-data/business-price-indexes-june-2020-quarter-corrections-to-previously-published-statistics.csv')]))
    # asset1 = assets.Asset('222', format='json', location=Location('url', parameters=[Parameter('url', 'https://api.exchangerate-api.com/v4/latest/USD')]))
    print(asset1.get_data())
