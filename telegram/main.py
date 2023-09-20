"""
    Script to send a message to a telegram channel using the user created telegram_api module
"""

from telegram_api import TelegramApi


def main():
    # create a class object
    telegram = TelegramApi()
    # create a test message
    warning_sign = bytes.decode(b"\xe2\x9a\xa0", "utf8")
    body = " This is a test message \n\n Go to: \n"
    url = "https://www.google.com/"
    msg = warning_sign + body + url
    # send the message to the telegram bot
    telegram.send_message(msg)


if __name__ == "__main__":
    main()
