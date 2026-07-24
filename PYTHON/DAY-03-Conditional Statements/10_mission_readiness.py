"""
Mini Project
Mission Readiness Checker
"""

fuel = float(input("Enter Fuel (kg): "))
weather = input("Enter Weather (Good/Bad): ")

if fuel >= 100 and weather.lower() == "good":
    print("\nMission Ready")
else:
    print("\nMission Delayed")