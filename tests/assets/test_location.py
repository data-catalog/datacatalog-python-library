from data_catalog.assets import Location
from data_catalog.client.asset import Parameter
import pytest


def test_get_parameters():
    location = Location('url', [Parameter('key1', 'value1')])

    assert location.get_parameter('key1') == 'value1'
    assert location.get_parameter('key2') is None


def test_get_parameters_when_parameters_is_none():
    location = Location('url')

    assert location.get_parameter('key') is None
