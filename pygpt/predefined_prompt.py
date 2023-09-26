"""
    Script to generate a random ChatGPT response
"""

import openai
import dotenv
import json

# load OpenAI API_KEY from .env file inside project folder
env_vars = dotenv.dotenv_values()
openai.api_key = env_vars["API_KEY"]


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
    # message = response.choices[0].text.strip()
    # choices returned correct output with errors
    # extract text after converting OpenAI obeject to json object
    json_message = json.loads(json.dumps(response, indent=4))
    # 'indent' adds pretty-printing for readability
    # extract text field
    message = json_message["choices"][0]["text"].strip()
    return message


def main():
    # random prompt to introduce a random person
    user_prompt = "Introduce yourself"
    # call function to get response from ChatGPT
    chatbot_response = get_chatgpt_response(user_prompt)
    # prints the response
    print("\n" + chatbot_response + "\n")


if __name__ == "__main__":
    # execute the main function
    main()
