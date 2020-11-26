import io

from azure.storage.blob import BlobServiceClient, ContainerClient
from PIL import Image

sas_token = "?sp=rl&st=2020-11-11T18:11:43Z&se=2020-11-12T18:11:43Z&sv=2019-12-12&sr=c&sig=PV8mMbg7L12Ka0juigwVISJZ2GEZU%2BXSwYTko0vNB78%3D"
container = ContainerClient(account_url="https://datacatalogblob.blob.core.windows.net", container_name="container", credential=sas_token)

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')

    image_data = container.download_blob(blob).readall()
    image = Image.open(io.BytesIO(image_data))
    image.show()
