from machine import ADC, Pin
import time

# Define ADC object on Pin 26
adc = ADC(Pin(26))

# Potentiometer parameters (adjust as needed)
voltage_reference = 3.3  # Reference voltage of the ADC
total_resistance = 10_000  # Total resistance of the potentiometer in ohms (10kΩ)

while True:
    # Read ADC value (0-65535)
    adc_value = adc.read_u16()

    # Convert ADC value to voltage
    voltage = (adc_value / 65535) * voltage_reference

    # Calculate resistance at the specific point
    resistance = (voltage / voltage_reference) * total_resistance

    # Print results
    print("ADC Value:", adc_value)
    print("Voltage:", voltage, "V")
    print("Resistance:", resistance, "ohms")

    # Optional: Add a delay to control the reading frequency
    time.sleep(5)  # Adjust the delay as needed