from machine import Pin
import utime

# Define the LED pin
led_pin = Pin(14, Pin.OUT)

# Function to blink the LED
def blink_led():
    led_pin.toggle()  # Toggle the LED state
    utime.sleep(0.1)    # Sleep for 1 second

# Main loop
while True:
    blink_led()
