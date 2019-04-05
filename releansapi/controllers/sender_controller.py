# -*- coding: utf-8 -*-

"""
    releansapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from releansapi.api_helper import APIHelper
from releansapi.configuration import Configuration
from releansapi.controllers.base_controller import BaseController
from releansapi.http.auth.o_auth_2 import OAuth2
from releansapi.models.response_200 import Response200
from releansapi.models.response_2001 import Response2001

class SenderController(BaseController):

    """A Controller to access Endpoints in the releansapi API."""


    def get_sender_name_details(self,
                                id,
                                accept):
        """Does a GET request to /sender/view/.

        Return the details of the sender name.

        Args:
            id (string): TODO: type description here. Example: 
            accept (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sender/view/'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def create_sender_name(self,
                           accept,
                           content_type,
                           body):
        """Does a POST request to /sender/create.

        Create a new sender id to send messages using it

        Args:
            accept (string): TODO: type description here. Example: 
            content_type (string): TODO: type description here. Example: 
            body (string): TODO: type description here. Example: 

        Returns:
            Response200: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sender/create'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=body)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response200.from_dictionary)

    def get_all_senders(self,
                        accept):
        """Does a GET request to /sender.

        List all senders names associated with the account

        Args:
            accept (string): TODO: type description here. Example: 

        Returns:
            list of Response2001: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sender'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response2001.from_dictionary)