#!/usr/bin/env python
import paho.mqtt.client as mqtt
import numpy as np


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test/#")


def on_message(client, userdata, msg):
    global count
    count = float(msg.payload)
    check_payload()


def generate_condition(arr):
    """
        The function generates if else condition based on the frequency of notifications.
        The if condition always begins with the largest inactivity. The last elif is therefore a condition,
        using the smallest inactivity, the user need to be aware of. The position of each element as well as the
        array length is used to assign values for flag. The smallest inactivity i.e the last elseif must assign False
        to boolean variable. This boolean variable is inverted as we move towards the top of the if statement.
    """
    code = """"""
    for i, j in enumerate(arr):
        if i == 0:
            text = 'if count > ' + str(j) + ':\n'
            if len(arr) % 2 == 0:
                text += '    flip('+str((i+1) % 2 != 0)+')\n'
            else:
                text += '    flip('+str((i+1) % 2 == 0)+')\n'
        else:
            text = 'elif count > ' + str(j) + ':\n'
            if len(arr) % 2 == 0:
                text += '    flip('+str((i+1) % 2 != 0)+')\n'
            else:
                text += '    flip('+str((i+1) % 2 == 0)+')\n'
        code += text
    return code


def exec_payload():
    """
        Function that operates on the reported inactivity payload.
        Can be used for printing, telegram alerting, etc.
    """
    global count
    unit = 'minutes' if count < 1 else 'hours'
    value = count*60 if count < 1 else count
    print('The elevator is inactive for the last %s %s' %(value, unit))


def flip(var):
    """
    Once the if else condition is satisfied, the current flag is inverted.
    This is to ensure that we only get a single notification, each time a condition is passed.
    """
    global flag
    if flag == var:
        exec_payload()
        flag = not var


def check_payload():
    """
    Executes the code generated from generate_condition().
    The if else constrains are passed as parameters.

    """
    arr = [44/60, 0.99, 1.99, 2.99, 3.99, 7.99, 9.99]
    code = generate_condition(arr[::-1])  # we pass the array in descending order, eg: [24 hrs, 12hrs, 6hrs, 3hrs]
    exec(code)


if 'flag' not in globals():
    flag = False


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
