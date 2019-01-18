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

class MessageController(BaseController):

    """A Controller to access Endpoints in the releans API."""

    def __init__(self, client=None, call_back=None):
        super(MessageController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_all_messages(self):
        """Does a GET request to /message.

        List all messages sent by the account.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_all_messages called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_all_messages.')
            _url_path = '/message'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_all_messages.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_all_messages.')
            _request = self.http_client.get(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_all_messages')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_all_messages.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for get_all_messages. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_price_of_message(self,
                             mobile_number):
        """Does a GET request to /message/price.

        Return cost of sending a message to the number.

        Args:
            mobile_number (string): Mobile number you want to know the price
                of sending a message.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_price_of_message called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for get_price_of_message.')
            self.validate_parameters(mobile_number=mobile_number)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_price_of_message.')
            _url_path = '/message/price'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_parameters = {
                'mobileNumber': mobile_number
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_price_of_message.')
            _request = self.http_client.get(_query_url)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_price_of_message')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_price_of_message.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for get_price_of_message. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return _context.response.raw_body

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_view_message(self,
                         id):
        """Does a GET request to /message/view.

        Return the details of the message.

        Args:
            id (string): Id of the message you need to return its details.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_message called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for get_view_message.')
            self.validate_parameters(id=id)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_message.')
            _url_path = '/message/view'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_parameters = {
                'id': id
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_view_message.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_view_message.')
            _request = self.http_client.get(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_view_message')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_message.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for get_view_message. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_send_sms_message(self,
                                sender_id,
                                mobile_number,
                                message):
        """Does a POST request to /message/send.

        Send a single message.

        Args:
            sender_id (string): Sender id to send the message from.
            mobile_number (string): The mobile number supposed to receive the
                message.
            message (string): Message text.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_send_sms_message called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for create_send_sms_message.')
            self.validate_parameters(sender_id=sender_id,
                                     mobile_number=mobile_number,
                                     message=message)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_send_sms_message.')
            _url_path = '/message/send'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare form parameters
            self.logger.info('Preparing form parameters for create_send_sms_message.')
            _form_parameters = {
                'senderId': sender_id,
                'mobileNumber': mobile_number,
                'message': message
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_send_sms_message.')
            _request = self.http_client.post(_query_url, parameters=_form_parameters)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'create_send_sms_message')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_send_sms_message.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for create_send_sms_message. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return _context.response.raw_body

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
