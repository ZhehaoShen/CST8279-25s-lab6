# Name: Zhehao Shen
# Student Number: 041145921
# Date: 2025-6-30
# Description: CST8279-lab6
import math

def CelToFahr(cel):
    fahr = (cel * 1.8) + 32
    return fahr

def FahrToCel(fahr):
    cel = (fahr - 32) / 1.8
    return cel

def min(a, b):
    if a <= b:
        return a
    else:
        return b

def VolumeOfSphere(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


def main():
    print("This program will:")
    print("1. Convert two temperatures from Celsius to Fahrenheit")
    print("2. Find the minimum of the two converted temperatures")
    print("3. Use the minimum temperature as radius to calculate sphere volume")
    # print()

    try:
        print("Enter two temperatures in Celsius:")
        temp1_cel = float(input("First temperature (°C): "))
        temp2_cel = float(input("Second temperature (°C): "))

        temp1_fahr = CelToFahr(temp1_cel)
        temp2_fahr = CelToFahr(temp2_cel)

        print(f"\nTemperature conversions:")
        print(f"{temp1_cel}°C = {temp1_fahr}°F")
        print(f"{temp2_cel}°C = {temp2_fahr}°F")

        min_temp = min(temp1_fahr, temp2_fahr)
        print(f"\nMinimum temperature: {min_temp:.2f}°F")

        # Use minimum temperature as radius for sphere volume
        radius = abs(min_temp)
        volume = VolumeOfSphere(radius)
        print(f"Volume of sphere = {volume} cubic units")

        print(f"\nSummary:")
        print(f"• Input temperatures: {temp1_cel}°C and {temp2_cel}°C")
        print(f"• Converted to: {temp1_fahr}°F and {temp2_fahr}°F")
        print(f"• Minimum: {min_temp}°F")
        print(f"• Sphere volume with radius {radius}: {volume} cubic units")

    except ValueError:
        print("Error: Please enter valid numbers for temperatures.")

main()