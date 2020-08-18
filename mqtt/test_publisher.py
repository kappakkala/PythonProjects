#!/usr/bin/env python
import time
import random
import json
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    time.sleep(2)
    msg = json.dumps({"temp": random.uniform(20,50)})
    client.publish("test/temperature", msg)
