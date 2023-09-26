# Querying ChatGPT with Python 

## Steps involved

### 0. Initial Setup

Create a virtual environment inside the project directory `virtualenv --python C:\Users\<username>\Anaconda3\python.exe venv`

Activate the environment `.\venv\Scripts\activate`

Copy **requirements.txt** into project directory and install the required packages using `pip install -r requirements.txt --upgrade`

Copy api key from OpenAI account. Refer [Tutorial](https://blog.enterprisedna.co/how-to-use-chatgpt-for-python/) and [Issue](https://community.openai.com/t/openai-error-invalidrequesterror-this-is-a-chat-model-and-not-supported-in-the-v1-completions-endpoint-did-you-mean-to-use-v1-chat-completions/314977).

### 1. Get response from ChatGPT using a predefined prompt

Set up **introduction.py**.

Optionally, improve code quality using *flake8* and *black*: `flake8 .\introduction.py` and `black .\introduction.py`.

Run **introduction.py**.

Here's a sample output
![](./images/output_introduction_py.png?raw=true "output")

