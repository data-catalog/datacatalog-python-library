# coding: utf-8

"""
    Data Catalog Versioning Service API

    The asset versioning service of the Data Catalog application.  Provides API endpoints to create, delete and retrieve asset versions. The access rights to an asset's version are the same as the right to the asset itself.  The versions cannot be modified, only deleted.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: szilardtumo@stud.ubbcluj.ro
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_catalog.client.versioning.configuration import Configuration


class ContentResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'last_modified': 'datetime',
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'last_modified': 'lastModified',
        'size': 'size'
    }

    def __init__(self, name=None, last_modified=None, size=None, local_vars_configuration=None):  # noqa: E501
        """ContentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._last_modified = None
        self._size = None
        self.discriminator = None

        self.name = name
        self.last_modified = last_modified
        if size is not None:
            self.size = size

    @property
    def name(self):
        """Gets the name of this ContentResponse.  # noqa: E501

        The name of the blob in the container.  # noqa: E501

        :return: The name of this ContentResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentResponse.

        The name of the blob in the container.  # noqa: E501

        :param name: The name of this ContentResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def last_modified(self):
        """Gets the last_modified of this ContentResponse.  # noqa: E501

        The date when the blob was last modified.  # noqa: E501

        :return: The last_modified of this ContentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ContentResponse.

        The date when the blob was last modified.  # noqa: E501

        :param last_modified: The last_modified of this ContentResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

    @property
    def size(self):
        """Gets the size of this ContentResponse.  # noqa: E501

        The size of the blob in bytes.  # noqa: E501

        :return: The size of this ContentResponse.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ContentResponse.

        The size of the blob in bytes.  # noqa: E501

        :param size: The size of this ContentResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 0):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentResponse):
            return True

        return self.to_dict() != other.to_dict()
