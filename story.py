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

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("the squirrel went down easy, but a wizard gives way behind the trees")
    print("the wizard asks, 'would you like to know the ways of wizardy?' ")
    choice = input("would you like to know the ways of wizardry? (yes/no): ").strip().lower()
    if choice == "yes":
        print("the wizard, instead of teaching you, takes possession of your body and your now only a backseat driver to your own body...")
        print("the wizard tames a dragon, and teleports both the dragon and the body to a new place, in a cave.")
        print("someone.. similar walks in. you start to realize its you but from a different universe.")
        print("the wizard triumphs over this alternate reality of you, and takes over the world")
    elif choice == "no":
        print("you say no, and take the wizards spell book and run deeper into the forest")
        print("distracted from reading the book, a dragon sneaks up on you!")
        print("not knowing what a single spell does, you ramble off a couple lines until you get the dragon to calm down.. it almost seems as if you tamed it")
        print("you try a 'teleportation' spell of sorts and it transports you and the dragon to a cave.. odd")
        print("you hear someone approaching the cave, thinking the wizard has sent someone for you.")
        print("you waste no time and slay the person before, but as you come to remove their helmet, you realize.. its you")
    print("as you live the rest of your life, you think about what happened and if anything makes sense anymore..")

if __name__ == "__main__":
    intro()
