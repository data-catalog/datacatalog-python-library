from configloader import ConfigLoader

from data_catalog.client.asset import Configuration
import os


def load():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, 'config.yaml')

    config = ConfigLoader()
    config.update_from_yaml_file(config_path)

    return Configuration(host=config['host'])
