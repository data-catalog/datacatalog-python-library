import pandas as pd

from data_catalog.models import Asset, Location
from data_catalog.services import AssetService
from data_catalog.client.asset import ParameterDto, ApiException

import pytest


@pytest.fixture
def asset_list():
    return [
        Asset(
            '0',
            created_at='2019-08-24T14:15:22Z',
            updated_at='2019-08-24T14:15:22Z',
            name='Iris Dataset',
            description='This is perhaps the best known database to be found in the pattern recognition literature. '
                        'Fishers paper is a classic in the field and is referenced frequently to this day. (See Duda & '
                        'Hart, for example.) The data set contains 3 classes of 50 instances each, where each class '
                        'refers to a type of iris plant. One class is linearly separable from the other 2; the latter '
                        'are '
                        'NOT linearly separable from each other.',
            location=Location('url', parameters=[ParameterDto('url', 'https://example.com')]),
            tags=['multivariate'],
            format='csv',
        ),
        Asset(
            '222',
            format='json',
            location=Location('url', parameters=[ParameterDto('url', 'https://api.exchangerate-api.com/v4/latest/USD')])
        ),
        Asset(
            '223',
            format='csv',
            location=Location('url', parameters=[ParameterDto('invalid', 'random')]))
    ]


def test_get_asset(mocker, asset_list):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_asset',
        return_value=asset_list[0]
    )

    with AssetService() as asset_service:
        assert asset_service.get_asset('0') == asset_list[0]


def test_get_asset_id_not_found(mocker):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_asset',
        side_effect=ApiException(status=404, reason='Not Found')
    )

    with AssetService() as asset_service:
        assert asset_service.get_asset('0') is None


def test_get_asset_api_call_error(mocker):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_asset',
        side_effect=ApiException(status=500, reason='Internal Server Error')
    )

    with AssetService() as asset_service:
        with pytest.raises(ApiException):
            asset_service.get_asset('0')


def test_list_assets(mocker, asset_list):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        assert asset_service.list_assets() == asset_list


def test_list_assets_dict(mocker, asset_list):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        assets = asset_service.list_assets(output_format='dict')

        assert type(assets) is dict
        assert assets['222'].format == 'json'


def test_list_assets_dataframe(mocker, asset_list):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        assets = asset_service.list_assets(output_format='dataframe')

        assert type(assets) is pd.DataFrame
        assert assets.at['222', 'format'] == 'json'


def test_list_assets_invalid_listing(mocker, asset_list):
    mocker.patch(
        'data_catalog.services.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        with pytest.raises(ValueError):
            asset_service.list_assets(output_format='invalid')
