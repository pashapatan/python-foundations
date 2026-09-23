print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choose_direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n" )
if choose_direction == "left":
    selection=input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n "  )
    if selection == "wait":
        door_selection=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which would you choose?\n")
        if door_selection == "red":
            print("It's a room full of fire. Game Over.")
        elif door_selection == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
