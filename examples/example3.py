import io

from azure.storage.blob import BlobServiceClient, ContainerClient
from PIL import Image

import data_catalog.assets.asset as asset
from data_catalog.client.asset import Parameter

sas_token = "?sp=racwdl&st=2020-12-02T12:36:52Z&se=2020-12-20T12:36:00Z&sv=2019-12-12&sr=c&sig=0kcSx2JVyHKZ2qnmqhpWb654Cn6uQtNSClLWQ3mG8L0%3D"
container = ContainerClient(account_url="https://datacatalogblob.blob.core.windows.net", container_name="container", credential=sas_token)

blob_asset = asset.Asset('222', format='csv', location=asset.Location('azureblob', parameters=[
        Parameter('accountUrl', 'https://datacatalogblob.blob.core.windows.net'),
        Parameter('containerName', 'container'),
        Parameter('sasToken', 'Q0cS0Cj4LyWy/unaxqD4BWp2niZ7WPzHC8ABEQWBnQ24qFENIBStCtk68T+QZaFxmS5pUqSd+ia8hH2fyYV1PQ=='),
        Parameter('expiryTime', '2020-12-20T12:36:00Z')
    ]))

blob = container.get_blob_client('nested/more nested/more nested user.csv')
print(blob.get_blob_properties())
print(blob)
for item in container.list_blobs():
    print(item)
