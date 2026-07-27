"""
Mini Project 2
Space Mission Readiness Checker
Author: Ezhumalai
"""

# Get fuel amount
fuel = float(input("Enter Fuel (kg): "))

# Get weather condition
weather = input("Enter Weather (Good/Bad): ")

# Check mission readiness
if fuel >= 100 and weather.lower() == "good":
    print("\n========== MISSION STATUS ==========")
    print("Mission Ready for Launch")
    print("====================================")
else:
    print("\n========== MISSION STATUS ==========")
    print("Mission Delayed")
    print("====================================")