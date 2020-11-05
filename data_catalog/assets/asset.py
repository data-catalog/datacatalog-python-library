import pandas as pd

from data_catalog.assets import Location
from data_catalog.client import AssetResponse


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

    def get_data(self) -> pd.DataFrame:
        if self.location is None:
            raise ValueError('Asset location is not defined')

        if self.location.type != 'url':
            raise NotImplementedError

        return self._get_data_from_url()

    def _get_data_from_url(self):
        url = self.location.get_parameter('url')
        if url is None:
            raise ValueError('Location has no url parameter')

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
