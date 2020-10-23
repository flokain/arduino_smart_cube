# coding: utf-8
import logging
from smartcube.models.base_model_ import Model
from smartcube.models.http_request import HttpRequest  # noqa: F401,E501
from smartcube import util
from urequests import request
log = logging.getLogger(__name__)


class Handler(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, request: HttpRequest = None, expected_response: int = 200
    ):  # noqa: E501
        """Handler - a model defined in Swagger

        :param request: The request of this Handler.  # noqa: E501
        :type request: HttpRequest
        :param expected_response: The expected_response of this Handler.  # noqa: E501
        :type expected_response: int
        """
        self.swagger_types = {"request": HttpRequest, "expected_response": int}

        self.attribute_map = {
            "request": "request",
            "expected_response": "expectedResponse",
        }
        self._request = request
        self._expected_response = expected_response

    @classmethod
    def from_dict(cls, dikt) -> "Handler":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Handler of this Handler.  # noqa: E501
        :rtype: Handler
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request(self) -> HttpRequest:
        """Gets the request of this Handler.


        :return: The request of this Handler.
        :rtype: HttpRequest
        """
        return self._request

    @request.setter
    def request(self, request: HttpRequest):
        """Sets the request of this Handler.


        :param request: The request of this Handler.
        :type request: HttpRequest
        """
        if request is None:
            raise ValueError(
                "Invalid value for `request`, must not be `None`"
            )  # noqa: E501

        self._request = request

    @property
    def expected_response(self) -> int:
        """Gets the expected_response of this Handler.


        :return: The expected_response of this Handler.
        :rtype: int
        """
        return self._expected_response

    @expected_response.setter
    def expected_response(self, expected_response: int):
        """Sets the expected_response of this Handler.


        :param expected_response: The expected_response of this Handler.
        :type expected_response: int
        """

        self._expected_response = expected_response

    def run(self):
        r = self._request
        response = request(method=r.method, url=r.uri, json=r.json, headers=r.headers)

        log.debug(
            "http request %s returned %i. exoected %i",
            r.uri,
            response.status_code,
            self._expected_response,
        )

        assert response.status_code == self._expected_response