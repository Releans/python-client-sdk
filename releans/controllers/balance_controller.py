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

class BalanceController(BaseController):

    """A Controller to access Endpoints in the releans API."""

    def __init__(self, client=None, call_back=None):
        super(BalanceController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_balance(self):
        """Does a GET request to /balance.

        Get your available balance

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_balance called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_balance.')
            _url_path = '/balance'
            _query_builder = Configuration.base_uri
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_balance.')
            _request = self.http_client.get(_query_url)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_balance')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_balance.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for get_balance. Returning nil.')
                return None
            self.validate_response(_context)
    
            # Return appropriate type
            return _context.response.raw_body

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
