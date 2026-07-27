"""
Mini Project
Satellite Speed Calculator
"""

speed = float(input("Enter Satellite Speed (km/s): "))
time = float(input("Enter Time (seconds): "))

distance = speed * time

print("\n===== RESULT =====")
print("Satellite Speed :", speed, "km/s")
print("Time            :", time, "seconds")
print("Distance        :", distance, "km")