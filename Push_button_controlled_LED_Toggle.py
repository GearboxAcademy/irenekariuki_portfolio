from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.on()
    else:
        led.off()