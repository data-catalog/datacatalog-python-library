from data_catalog.client.asset import Configuration

_access_token: str

_config = {
    'user_service': {
        'client_side_validation': False,
        'host': 'https://userhandlingservice.azurewebsites.net',
    },
    'asset_service': {
        'host': 'https://assethandlingservice.azurewebsites.net',
    },
    'versioning_service': {
        'host': 'https://versioningservice.azurewebsites.net',
    },
}


def set_access_token(access_token: str):
    globals()['_access_token'] = access_token


def _get_config(config_name: str):
    global _access_token, _config

    final_config = Configuration(host=_config[config_name].get('host'))
    final_config.client_side_validation = _config.get('client_side_validation')
    final_config.access_token = globals().get('_access_token')

    return final_config


def get_user_service_config():
    return _get_config('user_service')


def get_asset_service_config():
    return _get_config('asset_service')


def get_versioning_service_config():
    return _get_config('versioning_service')
