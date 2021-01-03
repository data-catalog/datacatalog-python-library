from azure.storage.blob import ContainerClient
from freezegun import freeze_time

import pytest
import pandas as pd

from data_catalog.assets import Asset, Location
from data_catalog.assets.version import Version
from data_catalog.client.asset import AssetResponse, Location as ClientLocation, Parameter
from data_catalog.client.versioning import ContentResponse


@pytest.fixture
def asset_response():
    return AssetResponse('222', format='json', location=ClientLocation('url', parameters=[
        Parameter('url', 'https://api.exchangerate-api.com/v4/latest/USD')]))


@pytest.fixture
def csv_asset():
    return Asset('222', format='csv', location=Location('url', parameters=[
        Parameter('url',
                  'https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-June-2020'
                  '-quarter/Download-data/business-price-indexes-june-2020-quarter-corrections-to-previously'
                  '-published-statistics.csv')]))


@pytest.fixture
def json_asset():
    return Asset('222', format='json', location=Location('url', parameters=[
        Parameter('url', 'https://api.exchangerate-api.com/v4/latest/USD')]))


@pytest.fixture
def blob_asset():
    return Asset('222', format='csv', location=Location('azureblob', parameters=[
        Parameter('accountUrl', 'https://datacatalogblob.blob.core.windows.net'),
        Parameter('containerName', 'container'),
        Parameter('sasToken', 'sas'),
        Parameter('containerName', 'container'),
        Parameter('expiryTime', '2020-11-17T17:10:50Z')
    ]))


@pytest.fixture
def version_list():
    return [
        Version(
            name='version1',
            asset_id='222',
            contents=[
                ContentResponse(id='111', name='file1', last_modified='2020-11-17T17:10:50Z')
            ],
            created_at='2020-11-17T17:10:50Z',
        ),
        Version(
            name='version2',
            asset_id='222',
            contents=[
                ContentResponse(id='111', name='file1', last_modified='2020-11-17T17:10:50Z'),
                ContentResponse(id='112', name='file1=2', last_modified='2020-11-17T17:10:50Z')
            ],
            created_at='2020-11-17T17:10:50Z',
        )
    ]


def test_from_response(asset_response):
    asset = Asset.from_response(asset_response)
    assert type(asset) == Asset
    assert hasattr(asset, 'get_data') is True


def test_get_data_from_url_csv(mocker, csv_asset):
    mocker.patch(
        'data_catalog.assets.asset.pd.read_csv',
        return_value='dataframe'
    )

    assert csv_asset._get_data_from_url() == 'dataframe'


def test_get_data_from_url_json(mocker, json_asset):
    mocker.patch(
        'data_catalog.assets.asset.pd.read_json',
        return_value='dataframe'
    )

    assert json_asset._get_data_from_url() == 'dataframe'


def test_get_data_from_url_no_url():
    asset = Asset('222', format='csv', location=Location('url', parameters=[
        Parameter('invalid', 'random')]))

    with pytest.raises(ValueError):
        asset.get_data()


def test_get_data_from_container_lacking_params():
    asset = Asset('222', format='container', location=Location('azureblob', parameters=[
        Parameter('accountUrl', 'https://datacatalogblob.blob.core.windows.net'),
        Parameter('containerName', 'container'),
        Parameter('expiryTime', '2020-11-17T17:10:50Z')
    ]))

    with pytest.raises(ValueError):
        asset.get_data()


@freeze_time("2020-11-18")
def test_get_data_from_container_when_expired(blob_asset):
    with pytest.raises(ValueError):
        blob_asset.get_data()


@freeze_time("2020-11-16")
def test_get_container_successful(blob_asset):
    assert type(blob_asset._get_container()) is ContainerClient


@freeze_time("2020-11-16")
def test_get_data_from_container_when_empty(mocker, blob_asset):
    mocker.patch(
        'data_catalog.assets.asset.ContainerClient.list_blobs',
        return_value=[]
    )

    with pytest.raises(ValueError):
        blob_asset.get_data()


def test_get_data(mocker, json_asset):
    mocker.patch(
        'data_catalog.assets.asset.Asset._get_data_from_url',
        return_value='dataframe'
    )

    assert json_asset.get_data() == 'dataframe'


def test_get_data_invalid():
    asset = Asset('222', format='csv', location=Location('invalid', parameters=[
        Parameter('url', 'random')]))

    with pytest.raises(NotImplementedError):
        asset.get_data()


def test_get_data_no_location():
    asset = Asset('222', format='csv')

    with pytest.raises(ValueError):
        asset.get_data()


def test_list_versions(mocker, version_list, blob_asset):
    mocker.patch(
        'data_catalog.assets.asset.VersionService.list_versions',
        return_value=version_list
    )

    versions = blob_asset.list_versions()
    assert versions == version_list


def test_get_version(mocker, version_list, blob_asset):
    mocker.patch(
        'data_catalog.assets.asset.VersionService.get_version',
        return_value=version_list[0]
    )

    version = blob_asset.get_version('version1')
    assert version == version_list[0]


def test_create_version(mocker, blob_asset):
    mocker.patch(
        'data_catalog.assets.asset.VersionService.create_version',
        return_value=None
    )

    assert blob_asset.create_version() is None


def test_delete_version(mocker, blob_asset):
    mocker.patch(
        'data_catalog.assets.asset.VersionService.delete_version',
        return_value=None
    )

    assert blob_asset.delete_version('version') is None
