from azure.storage.blob import ContainerClient

from data_catalog.assets import Asset, Location
from data_catalog.client.asset import Parameter

sas_token = "?sp=racwdl&st=2020-12-02T12:36:52Z&se=2020-12-20T12:36:00Z&sv=2019-12-12&sr=c&sig=0kcSx2JVyHKZ2qnmqhpWb654Cn6uQtNSClLWQ3mG8L0%3D"
container = ContainerClient(account_url="https://datacatalogblob.blob.core.windows.net", container_name="container", credential=sas_token)

blob_asset = Asset('222', format='csv', location=Location('azureblob', parameters=[
    Parameter('accountUrl', 'https://datacatalogblob.blob.core.windows.net'),
    Parameter('containerName', 'container'),
    Parameter('sasToken', 'Q0cS0Cj4LyWy/unaxqD4BWp2niZ7WPzHC8ABEQWBnQ24qFENIBStCtk68T+QZaFxmS5pUqSd+ia8hH2fyYV1PQ=='),
    Parameter('expiryTime', '2020-12-20T12:36:00Z')
]))

print(blob_asset.get_data())
