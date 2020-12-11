from typing import List, Dict, Union
import pandas as pd

from data_catalog import configloader
from data_catalog.assets.version import Version
from data_catalog.client.versioning import ApiClient, VersionApi


class VersionService:
    def __init__(self):
        # Create an instance of the API Client
        self.api_client = ApiClient(configuration=configloader.load())

        # Create an instance of the API class
        self.version_api = VersionApi(self.api_client)

    def list_versions(self, asset_id: str, output_format: str = 'list') -> Union[List[Version], Dict[str, Version], pd.DataFrame]:
        version_responses = self.version_api.get_asset_versions(asset_id)
        versions = (Version.from_response(version) for version in version_responses)

        if output_format == 'list':
            return list(versions)
        elif output_format == 'dict':
            return {version.id: version for version in versions}
        elif output_format == 'dataframe':
            return pd.DataFrame((version.to_dict() for version in versions)).set_index('id')
        else:
            raise NotImplementedError
