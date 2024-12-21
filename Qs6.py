subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))

total_marks = subject1 + subject2 + subject3 + subject4
percentage = (total_marks / 400) * 100

print(f"\nTotal Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"
