years_of_service = float(input("Enter the years of service: "))

salary = float(input("Enter the salary of the employee: "))

if years_of_service > 10:
    bonus = salary * 0.10  
elif 6 <= years_of_service <= 10:
    bonus = salary * 0.08  
else:
    bonus = salary * 0.05  
    print(f"The bonus for the employee is: Rs {bonus:.2f}")