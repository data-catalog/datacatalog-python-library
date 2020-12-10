import pandas as pd
from freezegun import freeze_time

from data_catalog.assets import Asset, Location
from data_catalog.client.asset import AssetResponse, Location as ClientLocation, Parameter

import pytest


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
def test_get_data_from_container_successful(blob_asset):
    assert type(blob_asset.get_data()) is pd.DataFrame


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
