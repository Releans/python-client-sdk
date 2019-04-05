# -*- coding: utf-8 -*-

"""
    releansapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from releansapi.api_helper import APIHelper
from releansapi.configuration import Configuration
from releansapi.controllers.base_controller import BaseController
from releansapi.http.auth.o_auth_2 import OAuth2

class MessageController(BaseController):

    """A Controller to access Endpoints in the releansapi API."""


    def get_all_messages(self,
                         accept):
        """Does a GET request to /message.

        List all messages sent by the account.

        Args:
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
        _url_path = '/message'
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
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_view_message(self,
                         id,
                         accept):
        """Does a GET request to /message/view.

        Return the details of the message.

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
        _url_path = '/message/view'
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

    def create_send_sms_message(self,
                                accept,
                                sender_id,
                                mobile_number,
                                message):
        """Does a POST request to /message/send.

        Send a single message.

        Args:
            accept (string): TODO: type description here. Example: 
            sender_id (string): Sender id to send the message from.
            mobile_number (string): The mobile number supposed to receive the
                message.
            message (string): Message text.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/message/send'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': accept
        }

        # Prepare form parameters
        _form_parameters = {
            'senderId': sender_id,
            'mobileNumber': mobile_number,
            'message': message
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)