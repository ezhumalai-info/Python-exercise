"""
Mini Project
Student Grade Calculator
"""

marks = int(input("Enter Your Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n========== RESULT ==========")
print("Marks :", marks)
print("Grade :", grade)