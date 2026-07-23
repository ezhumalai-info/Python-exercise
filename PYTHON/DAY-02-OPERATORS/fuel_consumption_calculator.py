"""
Mini Project
Fuel Consumption Calculator
"""

initial_fuel = float(input("Enter Initial Fuel (kg): "))
fuel_used = float(input("Enter Fuel Used (kg): "))

remaining_fuel = initial_fuel - fuel_used

print("\n===== RESULT =====")
print("Initial Fuel   :", initial_fuel, "kg")
print("Fuel Used      :", fuel_used, "kg")
print("Remaining Fuel :", remaining_fuel, "kg")