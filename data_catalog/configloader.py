from configloader import ConfigLoader

from data_catalog.client.asset import Configuration
import os


def _load_config(config_name: str):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, 'config.yaml')

    config = ConfigLoader()
    config.update_from_yaml_file(config_path)

    final_config = Configuration(host=config[config_name]['host'])
    final_config.client_side_validation = config.get('client_side_validation')

    return final_config


def load_user_service_config():
    return _load_config('user_service')


def load_asset_service_config():
    return _load_config('asset_service')


def load_versioning_service_config():
    return _load_config('versioning_service')
