import pytest
import pandas as pd

from data_catalog.models.version import Version
from data_catalog.services.version_service import VersionService
from data_catalog.client.versioning import ContentResponse


@pytest.fixture
def version_list():
    return [
        Version(
            name='version1',
            asset_id='222',
            contents=[
                ContentResponse(name='file1', last_modified='2020-11-17T17:10:50Z')
            ],
            created_at='2020-11-17T17:10:50Z',
        ),
        Version(
            name='version2',
            asset_id='222',
            contents=[
                ContentResponse(name='file1', last_modified='2020-11-17T17:10:50Z'),
                ContentResponse(name='file1=2', last_modified='2020-11-17T17:10:50Z')
            ],
            created_at='2020-11-17T17:10:50Z',
        )
    ]


def test_get_version(mocker, version_list):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.get_asset_version',
        return_value=version_list[0]
    )

    with VersionService() as version_service:
        assert version_service.get_version(name='version1', asset_id='222') == version_list[0]


def test_list_versions(mocker, version_list):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.get_asset_versions',
        return_value=version_list
    )

    with VersionService() as version_service:
        assert version_service.list_versions(asset_id='222') == version_list


def test_list_versions_dict(mocker, version_list):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.get_asset_versions',
        return_value=version_list
    )

    with VersionService() as version_service:
        versions = version_service.list_versions(asset_id='222', output_format='dict')

        assert type(versions) is dict


def test_list_versions_dataframe(mocker, version_list):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.get_asset_versions',
        return_value=version_list
    )

    with VersionService() as version_service:
        versions = version_service.list_versions(asset_id='222', output_format='dataframe')

        assert type(versions) is pd.DataFrame


def test_list_versions_wrong_type(mocker, version_list):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.get_asset_versions',
        return_value=version_list
    )

    with VersionService() as version_service:
        with pytest.raises(ValueError):
            version_service.list_versions(asset_id='222', output_format='invalid')


def test_create_version(mocker):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.create_asset_version',
        return_value=None
    )

    with VersionService() as version_service:
        assert version_service.create_version('222') is None


def test_delete_version(mocker):
    mocker.patch(
        'data_catalog.services.version_service.VersionApi.delete_asset_version',
        return_value=None
    )

    with VersionService() as version_service:
        assert version_service.delete_version('222', 'version') is None
