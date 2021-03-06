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

class SystemConfig(object):
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
        'wifi_ssid': 'str',
        'change_delay': 'int'
    }

    attribute_map = {
        'wifi_ssid': 'wifiSSID',
        'change_delay': 'changeDelay'
    }

    def __init__(self, wifi_ssid=None, change_delay=3000):  # noqa: E501
        """SystemConfig - a model defined in Swagger"""  # noqa: E501
        self._wifi_ssid = None
        self._change_delay = None
        self.discriminator = None
        if wifi_ssid is not None:
            self.wifi_ssid = wifi_ssid
        if change_delay is not None:
            self.change_delay = change_delay

    @property
    def wifi_ssid(self):
        """Gets the wifi_ssid of this SystemConfig.  # noqa: E501

        the SSID of the connected Wifi  # noqa: E501

        :return: The wifi_ssid of this SystemConfig.  # noqa: E501
        :rtype: str
        """
        return self._wifi_ssid

    @wifi_ssid.setter
    def wifi_ssid(self, wifi_ssid):
        """Sets the wifi_ssid of this SystemConfig.

        the SSID of the connected Wifi  # noqa: E501

        :param wifi_ssid: The wifi_ssid of this SystemConfig.  # noqa: E501
        :type: str
        """

        self._wifi_ssid = wifi_ssid

    @property
    def change_delay(self):
        """Gets the change_delay of this SystemConfig.  # noqa: E501

        when the cube is tilted, sensors indicate many CubeState changes. to mittigate the detection of those unwanted events after the cube is tilted it must stand still for milliseconds in changeDelay  # noqa: E501

        :return: The change_delay of this SystemConfig.  # noqa: E501
        :rtype: int
        """
        return self._change_delay

    @change_delay.setter
    def change_delay(self, change_delay):
        """Sets the change_delay of this SystemConfig.

        when the cube is tilted, sensors indicate many CubeState changes. to mittigate the detection of those unwanted events after the cube is tilted it must stand still for milliseconds in changeDelay  # noqa: E501

        :param change_delay: The change_delay of this SystemConfig.  # noqa: E501
        :type: int
        """

        self._change_delay = change_delay

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
        if issubclass(SystemConfig, dict):
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
        if not isinstance(other, SystemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
