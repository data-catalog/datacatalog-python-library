from data_catalog import DataCatalog

api_key = 'LmHQ28ZzCUiMmKZ/vJE2ub+fzbO4JZ+HQdz6byAfyGQthG6mcRjsX9UNZq9GODdkJm/Tvib4/ONHzYo2AlI1QA=='
with DataCatalog(api_key=api_key) as asset_service:
    assets = asset_service.list_assets()
    print(len(assets))

    asset_service.get_asset('asdasd')

