from machine import Pin
from utime import sleep

object=Pin(0, Pin.IN)

while True:
    print(object.value())
    sleep(0.5)
    