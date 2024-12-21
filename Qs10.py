grade = float(input("Enter the grade: "))

if grade < 25:
    grade_letter = "D"
elif 25 <= grade < 45:
    grade_letter = "C"
elif 45 <= grade < 50:
    grade_letter = "B"
elif 50 <= grade < 60:
    grade_letter = "B+"
elif 60 <= grade < 80:
    grade_letter = "A"
else:  # grade above 80
    grade_letter = "A+"
    print(f"The grade is: {grade_letter}")