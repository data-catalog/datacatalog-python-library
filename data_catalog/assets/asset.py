from typing import Union

import pandas as pd
from datetime import datetime
from azure.storage.blob import ContainerClient

from data_catalog.assets import Location
from data_catalog.client.asset import AssetResponse


class Asset(AssetResponse):
    def __init__(self, id=None, created_at=None, updated_at=None, name=None, description=None, location=None, tags=None,
                 format=None, size=None, namespace=None, local_vars_configuration=None):

        super().__init__(id=id, created_at=created_at, updated_at=updated_at, name=name, description=description,
                         location=location, tags=tags, format=format, size=size, namespace=namespace,
                         local_vars_configuration=local_vars_configuration)

        if self.location is not None:
            self.location = Location(location.type, location.parameters)

    @staticmethod
    def from_response(asset_response: AssetResponse):
        asset_response.__class__ = Asset
        return asset_response

    def get_data(self) -> Union[pd.DataFrame, ContainerClient]:
        if self.location is None:
            raise ValueError('Asset location is not defined')

        # check location type
        if self.location.type == 'url':
            return self._get_data_from_url()
        elif self.location.type == 'azureblob':
            return self._get_data_container()
        else:
            raise NotImplementedError

    def _get_data_from_url(self) -> pd.DataFrame:
        # get url parameter from asset location
        url = self.location.get_parameter('url')
        if url is None:
            raise ValueError('Location has no url parameter')

        # check data format
        try:
            if self.format == 'csv':
                data_frame = pd.read_csv(url)
            elif self.format == 'json':
                data_frame = pd.read_json(url)
            else:
                raise NotImplementedError
        except pd.errors.ParserError:
            raise ValueError('Could not parse the data from the url')

        return data_frame

    def _get_data_container(self) -> ContainerClient:
        account_url = self.location.get_parameter('account_url')
        container_name = self.location.get_parameter('containerName')
        credential = self.location.get_parameter('sasToken')
        expiry_time = datetime\
            .strptime(self.location.get_parameter('expiryTime'), '%Y-%m-%dT%H:%M:%SZ')

        if None in [account_url, container_name, credential]:
            raise ValueError('Parameters missing to create the container.')

        if expiry_time > datetime.now():
            raise ValueError('SAS token expired!')

        return ContainerClient(account_url=account_url,
                               container_name=container_name,
                               credential=credential)
