# Querying ChatGPT with Python 

## Steps involved

### 0. Initial Setup

Create a virtual environment inside the project directory `virtualenv --python C:\Users\<username>\Anaconda3\python.exe venv`

Activate the environment `.\venv\Scripts\activate`

Copy **requirements.txt** into project directory and install the required packages using `pip install -r requirements.txt --upgrade`

Copy api key from OpenAI account. Refer [Tutorial](https://blog.enterprisedna.co/how-to-use-chatgpt-for-python/) and [Issue](https://community.openai.com/t/openai-error-invalidrequesterror-this-is-a-chat-model-and-not-supported-in-the-v1-completions-endpoint-did-you-mean-to-use-v1-chat-completions/314977).

### 1. Get response from ChatGPT using a predefined prompt

Set up **predefined_prompt.py**.

Optionally, improve code quality using *flake8* and *black*: `flake8 .\predefined_prompt.py` and `black .\predefined_prompt.py`.

Run **predefined_prompt.py**.

Here's a sample output
![](./images/output_predefined_prompt_py.png?raw=true "output_predefined_prompt")

### 2. Get response from ChatGPT using a user-driven manual prompt

Set up and run **manual_prompt.py**.

Here's a sample output
![](./images/output_manual_prompt_py.png?raw=true "output_manual_prompt")

### 3. ChatGPT Telegram bot integration

The idea is to create and establish connection to a ChatGPT based telegram chat bot using Python. The bot queries the chat input from the user and responds with a related ChatGPT result.

#### 3.1 Telegram setup

Create a telegram bot. See the section [How to Create a New Bot for Telegram](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot).

Refer [Telegrams official API documentation](https://core.telegram.org/api/obtaining_api_id) to get *api id* and *api hash*. 

Append the following to the **.env** file and replace <> with the associated telegram configuration.

```Dotenv
BOT_API_ID = "<telegram api id>"
BOT_API_HASH = "<telegram api hash>"
BOT_NAME = "<telegram bot name>"
```

#### 3.2 Python setup

Set up and run **telegrambot_prompt.py**. This command prompt will ask for the phone number associated with the bot. Once the phone number is entered, type in the telegram confirmation code to start the session. Approve the session on your phone (via Telegram app).

Now, the user is able to send ChatGPT queries via the bot and receive the associated ChatGPT response immediately.
