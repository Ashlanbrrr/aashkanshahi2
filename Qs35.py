print("Welcome to the Magic Forest!")

choice1 = input("Do you want to go 'north' or 'south'? ").strip().lower()

if choice1 == "south":
    print("Game Over")
elif choice1 == "north":
    choice2 = input("Do you want to 'cross the river' or 'follow the path'? ").strip().lower()
    
    if choice2 == "cross the river":
        print("Game Over")
    elif choice2 == "follow the path":
        choice3 = input("Choose between 'fairy', 'ogre', or 'elf': ").strip().lower()
        
        if choice3 == "ogre" or choice3 == "fairy":
            print("Game Over")
        elif choice3 == "elf":
            print("You Win! Congratulations, you have found the elf!")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")