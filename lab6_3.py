# Name: Zhehao Shen
# Student Number: 041145921
# Date: 2025-6-30
# Description: CST8279-lab6-3
import time
from adafruit_circuitplayground import cp

def CelToFahr(cel):
    fahr = (cel * 1.8) + 32
    return fahr

def FahrToCel(fahr):
    cel = (fahr - 32) * 1.8
    return cel

while True:
    if cp.button_a:
        print("Button A pressed!")
        cp.red_led = True
        
        # Get temperature from sensor
        temp_celsius = cp.temperature

        if cp.switch:
            temp_fahrenheit = CelToFahr(temp_celsius)
            print(f"Temperature: {temp_celsius}°C -> {temp_fahrenheit}°F")
        else:
            print(f"Temperature: {temp_fahrenheit}°F -> {temp_celsius}°C")

        time.sleep(0.1)
    else:
        cp.red_led = False
    