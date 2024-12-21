def treasure_hunt():
    print("Welcome to Treasure Land")
    
    direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
    if direction == "right":
        print("Game Over.")
        return
    
    action = input("You've come to a lake. Do you want to 'swim' or 'wait' for a boat? ").lower()
    if action == "swim":
        print("Game Over.")
        return

    door = input("You arrive at a house with three doors: red, blue, and yellow. Which color do you choose? ").lower()
    if door == "red" or door == "blue":
        print("Game Over.")
    elif door == "yellow":
        print("You Win!")
    else:
        print("Invalid choice. Game Over.")

treasure_hunt()