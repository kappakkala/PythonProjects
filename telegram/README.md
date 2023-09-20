# Send a messsage to a telegram bot using Python

## Steps involved
Create a virtual environment inside the project directory `virtualenv --python C:\Users\<username>\Anaconda3\python.exe venv`

Activate the environment `.\venv\Scripts\activate`

Install requirements `pip install -r requirements.txt --upgrade`

Create a telegram bot and get its api_key and chat_id. See [Tutorial](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e).

Create a **settings.yaml** configuration file 
```yaml
"api_key" : "<enter bot api key>"
"chat_id" : "<enter chat id of the bot>"
```

Run **main.py**

