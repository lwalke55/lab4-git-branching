def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("after picking up the sword you travel further down the path and find a village..")
    print("do you go in the village? (yes/no)")
    choice = input("do you go in the village? (yes/no): ").strip().lower()
    if choice == "yes":
        print("going into the village, you find armor and a quest log to slay a dragon")
        print("you delve deeper into the path and go inside a cave:")
        print("you encounter a dragon, controlled by an evil wizard!")
        print("with armor and preperation, the fight was a cinch and they both went down without a sweat.")
    elif choice == "no":
        print("you avoid the village, and continue to walk down the path.")
        print("you delve deeper into the path and go inside a cave:")
        print("you encounter a dragon, controlled by an evil wizard!")
        print("as you have no armor, the battle was tough but you prevailed and were able to slay the wizard and its dragon.")
    print("at the end of the day, you keep the dragons egg you found after defeating it and raise it as your own.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()
