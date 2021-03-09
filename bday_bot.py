import pandas as pd
from datetime import datetime
from telegram_api import TelegramApi

df_cal = pd.read_excel(r'C:/Users/kappakkala/Documents/Calendar.xlsx')
df_cal = df_cal.fillna(value="nothing")
event = df_cal.at[int(datetime.today().strftime('%d'))-1, datetime.today().strftime('%B')]

API_KEY = '' # Provide the bot api key 
CHAT_ID = '' # Provide the chat id of the bot/channel
telegram = TelegramApi(API_KEY, CHAT_ID)
body = "Notification: "
msg = body + event
if  event != 'nothing':
    telegram.send_message(msg)
