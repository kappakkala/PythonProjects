#!/usr/bin/env python

"""
    TelegramApi sends a message to a telegram client channel.
"""

import requests
from urllib.parse import urlencode

__author__ = "Pakkaran"
__copyright__ = "Copyright 2020"
__version__ = "1"
__maintainer__ = "Pakkaran"
__email__ = ""
__status__ = "Prototype"
__date__ = "02-07-2020"


class TelegramApi:
    """
        This is a class for sending a telegram message.

        Attributes:
            api_key (str): The api key of the telegram chat bot.
            chat_id (str): The message id of the channel, whose admin is the chat bot.
    """
    api_key = None
    chat_id = None

    def __init__(self, api_key, chat_id):
        """
            The constructor for TelegramApi class.

            Parameters:
                api_key (str): The api key of the telegram chat bot.
                chat_id (str): The message id of the channel, whose admin is the chat bot.
        """
        self.api_key = api_key
        self.chat_id = chat_id

    def send_message(self, msg):
        """
            The function to send a message to a telegram channel.

            Parameters:
                msg (str): The message to be send to the telegram channel.
        """
        endpoint = 'https://api.telegram.org/bot' + self.api_key + '/sendMessage'
        data = urlencode({"chat_id": self.chat_id,
                          "text": msg})
        lookup_url = f"{endpoint}?{data}"
        requests.get(lookup_url)
