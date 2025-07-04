# Name: Zhehao Shen
# Student Number: 041145921
# Date: 2025-6-30
# Description: CST8279-lab6-2
import time
from adafruit_circuitplayground import cp

def CelToFahr(cel):
    fahr = (cel * 1.8) + 32
    return fahr

def FahrToCel(fahr):
    cel = (fahr - 32) / 1.8
    return cel

while True:
    temp_celsius = cp.temperature
    # Switch is True
    if cp.switch:
        temp_fahrenheit = CelToFahr(temp_celsius)
        print(f"Temperature: {temp_celsius}°C -> {temp_fahrenheit}°F")
    # Switch is False
    else:
        temp_fahrenheit = CelToFahr(temp_celsius)
        temp_converted_celsius = FahrToCel(temp_fahrenheit)
        print(f"Temperature: {temp_fahrenheit}°F -> {temp_converted_celsius}°C")
    
    time.sleep(1)