from data_catalog.client.asset.models.location import Location as ClientLocation


class Location (ClientLocation):
    def __init__(self, type=None, parameters=None):
        super().__init__(type=type, parameters=parameters)

    def get_parameter(self, key):
        if self.parameters is None:
            return None

        values = [parameter.value for parameter in self.parameters if parameter.key == key]

        return values[0] if len(values) > 0 else None
