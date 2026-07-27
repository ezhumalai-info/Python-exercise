#Distance = Speed × Time
# ----------------------------------------
# Mini Project 1
# Satellite Speed Calculator
# ----------------------------------------

# Get satellite speed from the user
speed = float(input("Enter Satellite Speed (km/s): "))

# Get travel time from the user
time = float(input("Enter Time (seconds): "))

# Calculate distance
distance = speed * time

# Display the result
print("\n========== SATELLITE SPEED CALCULATOR ==========")
print("Satellite Speed :", speed, "km/s")
print("Travel Time     :", time, "seconds")
print("Distance Travelled :", distance, "km")
print("================================================")