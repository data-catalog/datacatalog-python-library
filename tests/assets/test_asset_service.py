import pandas as pd

from data_catalog.assets import Asset, Location, AssetService
from data_catalog.client.asset import Parameter

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
            location=Location('url', Parameter('url', 'http://example.com')),
            tags=['multivariate'],
            format='csv',
            size='25 MB',
            namespace='flowerproject',
        ),
        Asset(
            '222',
            format='json',
            location=Location('url', parameters=[Parameter('url', 'https://api.exchangerate-api.com/v4/latest/USD')])
        ),
        Asset(
            '223',
            format='csv',
            location=Location('url', parameters=[Parameter('invalid', 'random')]))
    ]


def test_get_asset(mocker, asset_list):
    mocker.patch(
        'data_catalog.assets.asset_service.AssetApi.get_asset',
        return_value=asset_list[0]
    )

    with AssetService() as asset_service:
        assert asset_service.get_asset('0') == asset_list[0]


@pytest.mark.skip(reason="the api endpoint's behaviour is undefined")
def test_get_asset_id_not_found(mocker):
    mocker.patch(
        'data_catalog.assets.asset_service.AssetApi.get_asset',
        return_value=None
    )

    with AssetService() as asset_service:
        assert asset_service.get_asset('0') is None


def test_list_assets(mocker, asset_list):
    mocker.patch(
        'data_catalog.assets.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        assert asset_service.list_assets() == asset_list


def test_list_assets_dict(mocker, asset_list):
    mocker.patch(
        'data_catalog.assets.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        assets = asset_service.list_assets(output_format='dict')

        assert type(assets) is dict
        assert assets['222'].format == 'json'


def test_list_assets_dataframe(mocker, asset_list):
    mocker.patch(
        'data_catalog.assets.asset_service.AssetApi.get_assets',
        return_value=asset_list
    )

    with AssetService() as asset_service:
        assets = asset_service.list_assets(output_format='dataframe')

        assert type(assets) is pd.DataFrame
        assert assets.at['222', 'format'] == 'json'
