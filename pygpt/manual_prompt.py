"""
    Script to generate a ChatGPT response based on a manual input prompt
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
    # extract text after converting OpenAI obeject to json object
    json_message = json.loads(json.dumps(response, indent=4))
    # 'indent' adds pretty-printing for readability
    # extract text field
    message = json_message["choices"][0]["text"].strip()
    return message


def main():
    cont = True
    while cont:
        # random prompt to introduce a random person
        user_prompt = input("\nEnter the ChatGPT prompt:\n")
        # call function to get response from ChatGPT
        chatbot_response = get_chatgpt_response(user_prompt)
        # prints the response
        print("\n" + chatbot_response + "\n")
        flag = input("Enter y/Y to continue.")
        if flag == "y" or flag == "Y":
            cont = True
        else:
            cont = False


if __name__ == "__main__":
    # execute the main function
    main()
