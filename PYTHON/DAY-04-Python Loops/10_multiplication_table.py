"""
Homework
Multiplication Table Generator
Author: Ezhumalai
"""

number = int(input("Enter a Number: "))

print("\nMultiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)