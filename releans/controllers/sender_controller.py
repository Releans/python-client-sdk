# -*- coding: utf-8 -*-

"""
    releans

    This file was automatically generated for Releans by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from releans.api_helper import APIHelper
from releans.configuration import Configuration
from releans.controllers.base_controller import BaseController
from releans.http.auth.o_auth_2 import OAuth2

class SenderController(BaseController):

    """A Controller to access Endpoints in the releans API."""

    def __init__(self, client=None, call_back=None):
        super(SenderController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_sender_name_details(self,
                                id):
        """Does a GET request to /sender/view/.

        Return the details of the sender name.

        Args:
            id (string): The sender id you want its details

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_sender_name_details called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for get_sender_name_details.')
            self.validate_parameters(id=id)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_sender_name_details.')
            _url_path = '/sender/view/'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_parameters = {
                'id': id
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_sender_name_details.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_sender_name_details.')
            _request = self.http_client.get(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_sender_name_details')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_sender_name_details.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for get_sender_name_details. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_sender_name(self,
                           sender_name):
        """Does a POST request to /sender/create.

        Create a new sender id to send messages using it

        Args:
            sender_name (string): Name you want to register as Sender Name

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_sender_name called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for create_sender_name.')
            self.validate_parameters(sender_name=sender_name)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_sender_name.')
            _url_path = '/sender/create'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_sender_name.')
            _headers = {
                'content-type': 'text/plain; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_sender_name.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=sender_name)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'create_sender_name')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_sender_name.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for create_sender_name. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return _context.response.raw_body

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_all_senders(self):
        """Does a GET request to /sender.

        List all senders names associated with the account

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_all_senders called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_all_senders.')
            _url_path = '/sender'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_all_senders.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_all_senders.')
            _request = self.http_client.get(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_all_senders')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_all_senders.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for get_all_senders. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
