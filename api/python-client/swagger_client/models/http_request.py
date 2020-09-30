# coding: utf-8

"""
    Smartcube API

    This APIis used to read and configure webhooks to be triggered by the sides of the cube  # noqa: E501

    OpenAPI spec version: v1
    Contact: flokain11@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HttpRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uri': 'str',
        'method': 'str',
        'headers': 'dict(str, str)',
        'payload': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'method': 'method',
        'headers': 'headers',
        'payload': 'payload'
    }

    def __init__(self, uri=None, method='GET', headers=None, payload=None):  # noqa: E501
        """HttpRequest - a model defined in Swagger"""  # noqa: E501
        self._uri = None
        self._method = None
        self._headers = None
        self._payload = None
        self.discriminator = None
        self.uri = uri
        if method is not None:
            self.method = method
        if headers is not None:
            self.headers = headers
        if payload is not None:
            self.payload = payload

    @property
    def uri(self):
        """Gets the uri of this HttpRequest.  # noqa: E501


        :return: The uri of this HttpRequest.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this HttpRequest.


        :param uri: The uri of this HttpRequest.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def method(self):
        """Gets the method of this HttpRequest.  # noqa: E501


        :return: The method of this HttpRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this HttpRequest.


        :param method: The method of this HttpRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def headers(self):
        """Gets the headers of this HttpRequest.  # noqa: E501


        :return: The headers of this HttpRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this HttpRequest.


        :param headers: The headers of this HttpRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def payload(self):
        """Gets the payload of this HttpRequest.  # noqa: E501


        :return: The payload of this HttpRequest.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this HttpRequest.


        :param payload: The payload of this HttpRequest.  # noqa: E501
        :type: str
        """

        self._payload = payload

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(HttpRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other