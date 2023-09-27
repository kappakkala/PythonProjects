"""
    Script to create a ChatGPT based chat bot in telegram
"""

import openai
import dotenv
import json
from telethon.sync import TelegramClient, events

# load variables from .env file inside project folder
env_vars = dotenv.dotenv_values()
openai.api_key = env_vars["API_KEY"]
api_id = int(str(env_vars["BOT_API_ID"]))
api_hash = str(env_vars["BOT_API_HASH"])
bot_name = env_vars["BOT_NAME"]


def get_chatgpt_response(message: str, model="gpt-3.5-turbo"):
    """
    The function sends a prompt to ChatGPT and returns the response.

    Parameters:
        message (str): The prompt that is sent to ChatGPT.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # extract text after converting OpenAI obeject to json object
    json_message = json.loads(json.dumps(response, indent=4))
    # 'indent' adds pretty-printing for readability

    # extract text field
    message = json_message["choices"][0]["text"].strip()
    return message


def run_telegram_client():
    """
    The function setups a telegram client.
    It queries from the bot and returns the response to the bot.
    https://stackoverflow.com/questions/56295761/how-to-get-a-message-from-telegram-groups-by-api
    """
    # create a new session
    client = TelegramClient("sessionX", api_id, api_hash)

    # if success, read input and return response
    @client.on(events.NewMessage(chats=bot_name))
    async def my_event_handler(event):
        # get prompt from the bot
        user_prompt = event.raw_text
        # call function to get response from ChatGPT
        chatbot_response = get_chatgpt_response(user_prompt)
        # send ChatGPT response to chatbot
        await event.reply(chatbot_response)

    # start the client
    client.start()
    # run the client until it is disconnected
    client.run_until_disconnected()


def main():
    # execute the telegram client
    run_telegram_client()


if __name__ == "__main__":
    main()
