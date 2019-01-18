# -*- coding: utf-8 -*-

"""
    releans

    This file was automatically generated for Releans by APIMATIC v2.0 ( https://apimatic.io ).
"""

import sys
import logging

from releans.api_helper import APIHelper

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # The base Uri for API calls
    base_uri = 'https://platform.releans.com/api'

    # OAuth 2.0 Access Token
    # TODO: Set an appropriate value
    o_auth_access_token = None

