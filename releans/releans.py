# -*- coding: utf-8 -*-

"""
    releans

    This file was automatically generated for Releans by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .decorators import lazy_property
from releans.configuration import Configuration
from releans.controllers.message_controller import MessageController
from releans.controllers.sender_controller import SenderController
from releans.controllers.balance_controller import BalanceController


class Releans(object):

    config = Configuration

    @lazy_property
    def message(self):
        return MessageController()

    @lazy_property
    def sender(self):
        return SenderController()

    @lazy_property
    def balance(self):
        return BalanceController()


    def __init__(self,
                 o_auth_access_token=None):
        if o_auth_access_token != None:
            Configuration.o_auth_access_token = o_auth_access_token


