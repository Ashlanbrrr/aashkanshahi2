correct_username = "user123"
correct_password = "pass123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username:
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Incorrect username. Please try again.")