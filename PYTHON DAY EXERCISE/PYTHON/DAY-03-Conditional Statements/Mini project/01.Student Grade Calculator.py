"""
Mini Project 1
Student Grade Calculator
Author: Ezhumalai
"""

# Get marks from the user
marks = int(input("Enter Your Marks: "))

# Check the grade
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

# Display the result
print("\n========== STUDENT GRADE REPORT ==========")
print("Marks :", marks)
print("Grade :", grade)
print("==========================================")