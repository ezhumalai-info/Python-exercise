#Distance = Speed × Time
speed = float(input("Enter Satellite Speed (km/s): "))

for time in range(1, 11):
    distance = speed * time
    print("Time:", time, "seconds", "| Distance:", distance, "km")