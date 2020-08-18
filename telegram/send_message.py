"""
    Script to send a message to a telegram channel using the user created telegram_api module
"""

from telegram_api import TelegramApi

API_KEY = '' # Provide the bot api key 
CHAT_ID = '' # Provide the chat id of the bot/channel
telegram = TelegramApi(API_KEY, CHAT_ID)
warning_sign = bytes.decode(b'\xe2\x9a\xa0', 'utf8')
body = " This is a test message \n Go to: \n"
url = 'https://www.google.com/'
msg = warning_sign + body + url
telegram.send_message(msg)
