# blinks two led alternately every second
from machine import Pin
from time import sleep

LED_BUILTIN1 = 2
LED_BUILTIN2 = 16

led1 = Pin(LED_BUILTIN1, Pin.OUT)
led2 = Pin(LED_BUILTIN2, Pin.OUT)

while True:
  led1.on()
  led2.off()
  sleep(1)
  led1.off()
  led2.on()
  sleep(1)