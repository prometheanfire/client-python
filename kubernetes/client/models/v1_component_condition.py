# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ComponentCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error=None, message=None, status=None, type=None):
        """
        V1ComponentCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error': 'str',
            'message': 'str',
            'status': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'error': 'error',
            'message': 'message',
            'status': 'status',
            'type': 'type'
        }

        self._error = error
        self._message = message
        self._status = status
        self._type = type

    @property
    def error(self):
        """
        Gets the error of this V1ComponentCondition.
        Condition error code for a component. For example, a health check error code.

        :return: The error of this V1ComponentCondition.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1ComponentCondition.
        Condition error code for a component. For example, a health check error code.

        :param error: The error of this V1ComponentCondition.
        :type: str
        """

        self._error = error

    @property
    def message(self):
        """
        Gets the message of this V1ComponentCondition.
        Message about the condition for a component. For example, information about a health check.

        :return: The message of this V1ComponentCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1ComponentCondition.
        Message about the condition for a component. For example, information about a health check.

        :param message: The message of this V1ComponentCondition.
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """
        Gets the status of this V1ComponentCondition.
        Status of the condition for a component. Valid values for \"Healthy\": \"True\", \"False\", or \"Unknown\".

        :return: The status of this V1ComponentCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1ComponentCondition.
        Status of the condition for a component. Valid values for \"Healthy\": \"True\", \"False\", or \"Unknown\".

        :param status: The status of this V1ComponentCondition.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this V1ComponentCondition.
        Type of condition for a component. Valid value: \"Healthy\"

        :return: The type of this V1ComponentCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ComponentCondition.
        Type of condition for a component. Valid value: \"Healthy\"

        :param type: The type of this V1ComponentCondition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ComponentCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
