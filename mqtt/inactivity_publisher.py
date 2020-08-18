#!/usr/bin/env python
import time
import numpy as np
import paho.mqtt.client as mqtt
from datetime import datetime, timedelta


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)
client.loop_start()
arr = []
for i in range(610): # maximum inactivity of 10.16 hours
    last_update = datetime.now()-timedelta(minutes=i)
    arr.append((datetime.now()-last_update).total_seconds()/3600)
for i in arr:
    client.publish("test/", str(i))
    print('Publishing '+str(i))
    time.sleep(1/10)
