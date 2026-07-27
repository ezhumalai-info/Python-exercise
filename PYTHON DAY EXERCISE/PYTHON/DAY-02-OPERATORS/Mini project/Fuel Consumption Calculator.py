#Remaining Fuel = Initial Fuel − Fuel Used
# ----------------------------------------
# Mini Project 2
# Fuel Consumption Calculator
# ----------------------------------------

# Get the initial fuel amount
initial_fuel = float(input("Enter Initial Fuel (kg): "))

# Get the amount of fuel used
fuel_used = float(input("Enter Fuel Used (kg): "))

# Calculate the remaining fuel
remaining_fuel = initial_fuel - fuel_used

# Display the result
print("\n========== FUEL CONSUMPTION CALCULATOR ==========")
print("Initial Fuel   :", initial_fuel, "kg")
print("Fuel Used      :", fuel_used, "kg")
print("Remaining Fuel :", remaining_fuel, "kg")
print("=================================================")