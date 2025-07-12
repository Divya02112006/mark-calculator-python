print("Welcome to My Mark Calculator")

# Input Section
name = input("Enter your name: ")
tamil = int(input("Enter the Tamil mark: "))
english = int(input("Enter the English mark: "))
maths = int(input("Enter the Maths mark: "))
science = int(input("Enter the Science mark: "))
social = int(input("Enter the Social mark: "))

# Calculation
total = tamil + english + maths + science + social
average = total / 5

# Grade logic
if average >= 90:
    grade = "A+"
elif average >= 70:
    grade = "B"
elif average >= 50: 
    grade = "C"
elif average >= 30:
    grade = "D"
else:
    grade = "Fail"

# Output
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
