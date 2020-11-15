from data_catalog.assets import Asset, Location
from data_catalog.client.asset import Parameter
from data_catalog.client.asset import ApiClient
import data_catalog.assets as assets

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
        'data_catalog.assets.functions.AssetApi.get_asset',
        return_value=asset_list[0]
    )

    with ApiClient() as api_client:
        assert assets.get_asset(api_client, '0') == asset_list[0]


@pytest.mark.skip(reason="the api endpoint's behaviour is undefined")
def test_get_asset_id_not_found(mocker):
    mocker.patch(
        'data_catalog.assets.functions.AssetApi.get_asset',
        return_value=None
    )

    with ApiClient() as api_client:
        assert assets.get_asset(api_client, '0') is None


def test_list_assets(mocker, asset_list):
    mocker.patch(
        'data_catalog.assets.functions.AssetApi.get_assets',
        return_value=asset_list
    )

    with ApiClient() as api_client:
        assert assets.list_assets(api_client) == asset_list
