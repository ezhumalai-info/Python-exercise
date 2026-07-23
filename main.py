"""
example--1
Mini Project 1 — Satellite Information System

Create a program that asks the user for:

Satellite Name
Country
Launch Year
Altitude (km)
Speed (km/s)

Then print the information neatly.
"""
import jupyter_server_terminals

satellite_name = input("Enter Satellite Name: ")
country = input("Enter Country: ")
launch_year = int(input("Enter Launch Year: "))
altitude = float(input("Enter Altitude (km): "))
speed = float(input("Enter Speed (km/s): "))


print("================Satellite Information System===================")
print("Satellite Name: ", satellite_name)
print("Country: ", country)
print("Launch Year: ", launch_year)
print("Altitude: ", altitude,"km")
print("Speed: ", speed,"km/s")

#Practice Exercises
print("===================Welcome to Space AI Engineer=======================")

#TASK ---------->1
#Create variables for your name, age, and college, then print them.
name=input("enter your name:")
age=input("enter your age:")
college=input("enter your college:")

print("===================TASK 1=======================")
print("name:",name)
print("age:",age)
print("college:",college)

#TASK ---------->2
#Create variables for a satellite's name, altitude, and speed.

satellite_name=input("Enter Satellite Name: ")
altitude=float(input("Enter Altitude (km): "))
speed=float(input("Enter Speed (km/s): "))

print("===================TASK 2=======================")
print("satellite_name:",satellite_name)
print("altitude:",altitude,"km")
print("speed:",speed,"km/s")

#TASK ---------->3
#Ask the user for their favorite planet and print it.
fav_planet=input("enter your favorite planet:")

print("===================TASK 3=======================")
print("fav_planet:",fav_planet)

#TASK ---------->4
#Convert a string "1500" to an integer and add 500.
number=int(input("enter your number:"))
number=int(number)
answer=number+500

print("===================TASK 4=======================")
print("original answer:",number)
print(("add 500:",answer))

#TASK ---------->5
#Display the data type of five different variables.

planet=("jupiter")
distance="250"
time=2.51
altitude=254

print("===================TASK 5=======================")
print(type(planet))
print(type(distance))
print(type(time))
print(type(altitude))

#TASK ---------->6
#Ask for a satellite launch year and calculate its age (assuming the current year is 2026).
satellite_year=2002
age=satellite_year-2026

print("===================TASK 6=======================")
print("satellite age:",age)

#TASK ---------->7
#Create variables for three planets and print them.
planet1= "earth"
planet2="mars"
planer3="jupiter"

print("===================TASK 7=======================")
print(planet1,planet2,planer3)


#TASK ---------->8
# Store the satellite name
satellite_name = "INSAT-3DR"

# Store the launch year
launch_year = 2016

# Store the orbit altitude in kilometers
altitude = 35786

print("===================TASK 8=======================")
# Print the satellite name
print("Satellite:", satellite_name)

# Print the launch year
print("Launch Year:", launch_year)

# Print the orbit altitude
print("Altitude:", altitude, "km")

#TASK ---------->9
# Create a "Mission Information" program with at least six variables.

mission_name = "Chandrayaan-3"
space_agency = "ISRO"
destination = "Moon"
launch_year = 2023
mission_duration = 14
rocket_name = "LVM3-M4"

print("Mission Name:", mission_name)
print("Space Agency:", space_agency)
print("Destination:", destination)
print("Launch Year:", launch_year)
print("Mission Duration:", mission_duration, "Days")
print("Rocket Name:", rocket_name)

#THESE TOPIC RELATED MINI PROJECT
"""
Create a Space Mission Profile program that stores and displays:

Mission Name
Space Agency
Destination
Launch Year
Mission Duration
Rocket Name
"""
# Skyroot Aerospace Mission Profile

company_name = "Skyroot Aerospace"
rocket_name = "Vikram-1"
mission_name = "Mission Aagaman"
launch_year = 2026
launch_site = "Satish Dhawan Space Centre, Sriharikota"
payload_capacity = 350
orbit = "Low Earth Orbit (450 km)"

print("========== SKYROOT AEROSPACE ==========")
print("Company Name     :", company_name)
print("Rocket Name      :", rocket_name)
print("Mission Name     :", mission_name)
print("Launch Year      :", launch_year)
print("Launch Site      :", launch_site)
print("Payload Capacity :", payload_capacity, "kg")
print("Target Orbit     :", orbit)
print("=======================================")

"""
Day 1 Status

You have completed:

✅ Python Basics
✅ Variables
✅ Data Types
✅ print()
✅ input()
✅ type()
✅ Type Conversion
✅ Comments
✅ Practice Exercises
✅ Mini Project
✅ Homework
✅ Revision
"""