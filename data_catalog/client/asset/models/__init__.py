# coding: utf-8

# flake8: noqa
"""
    Data Catalog Asset Service API

    The asset handling service of the Data Catalog application.  Provides API endpoints to create, delete, and modify assets. It also manages the access rights to the assets, as private assets are only available to users that are members of it.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: szilard.tumo@stud.ubbcluj.ro
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from data_catalog.client.asset.models.asset_creation_request import AssetCreationRequest
from data_catalog.client.asset.models.asset_response import AssetResponse
from data_catalog.client.asset.models.asset_update_request import AssetUpdateRequest
from data_catalog.client.asset.models.error_response import ErrorResponse
from data_catalog.client.asset.models.location_creation_request import LocationCreationRequest
from data_catalog.client.asset.models.location_response import LocationResponse
from data_catalog.client.asset.models.location_update_request import LocationUpdateRequest
from data_catalog.client.asset.models.parameter_dto import ParameterDto
