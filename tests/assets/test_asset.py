from data_catalog.assets import Asset, Location
from data_catalog.client.asset import AssetResponse, Location as ClientLocation, Parameter
import pytest
import pytest_mock


@pytest.fixture
def asset_response():
    return AssetResponse('222', format='json', location=ClientLocation('url', parameters=[
        Parameter('url', 'https://api.exchangerate-api.com/v4/latest/USD')]))


@pytest.fixture
def csv_asset():
    return Asset('222', format='csv', location=Location('url', parameters=[
        Parameter('url',
                  'https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-June-2020-quarter/Download-data/business-price-indexes-june-2020-quarter-corrections-to-previously-published-statistics.csv')]))


@pytest.fixture
def json_asset():
    return Asset('222', format='json', location=Location('url', parameters=[
        Parameter('url', 'https://api.exchangerate-api.com/v4/latest/USD')]))


@pytest.fixture
def invalid_asset():
    return Asset('222', format='csv', location=Location('invalid', parameters=[
        Parameter('url', 'random')]))


@pytest.fixture
def no_location_asset():
    return Asset('222', format='csv')


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


def test_get_data(mocker, json_asset):
    mocker.patch(
        'data_catalog.assets.asset.Asset._get_data_from_url',
        return_value='dataframe'
    )

    assert json_asset.get_data() == 'dataframe'


def test_get_data_invalid(invalid_asset):
    with pytest.raises(NotImplementedError):
        invalid_asset.get_data()


def test_get_data_no_location(no_location_asset):
    with pytest.raises(ValueError):
        no_location_asset.get_data()
