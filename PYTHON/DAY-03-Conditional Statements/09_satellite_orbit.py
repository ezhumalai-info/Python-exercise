"""
Homework
Satellite Orbit Classifier
"""

altitude = float(input("Enter Satellite Altitude (km): "))

if altitude < 200:
    print("Very Low Orbit")
elif altitude <= 2000:
    print("Low Earth Orbit (LEO)")
elif altitude <= 35786:
    print("Medium Earth Orbit (MEO)")
else:
    print("Geostationary Orbit (GEO)")