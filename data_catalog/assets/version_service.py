from typing import List, Dict, Union
import pandas as pd

from data_catalog import configloader
from data_catalog.assets.version import Version
from data_catalog.client.versioning import ApiClient, VersionApi


class VersionService:
    """
    A client to interact with the Version service.
    This client provides operations to list and find asset versions.
    """
    def __init__(self):
        """
        Constructor of the VersionService class.
        The configuration will be loaded from config.yaml.
        """
        # Create an instance of the API Client
        self.api_client = ApiClient(configuration=configloader.load())

        # Create an instance of the API class
        self.version_api = VersionApi(self.api_client)

    def list_versions(self, asset_id: str, output_format: str = 'list') -> \
            Union[List[Version], Dict[str, Version], pd.DataFrame]:
        """
        Lists every version of an asset.
        :param asset_id: The id of the requested asset.
        :param output_format: The format in which the versions will be listed.
        :return: All versions available.
                 If the output_format is 'list': returns a list of versions.
                 If the output_format is 'dict': returns a mapping from id to version as a dictionary.
                 If the output_format is 'dataframe': returns a pandas DataFrame, where each row represents a version,
                                                      the indexes are the ids, and the columns represent the attributes
                                                      of the version.
        """
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
