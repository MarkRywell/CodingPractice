name = input("Please enter player name: ")
age = 0
while age <= 10:
    age = int(input("Enter age: "))
    print()
    if age <= 10:
        print("Age Inappropriate!")

health = 10


def start():
    global name
    print("Welcome to Adventure of " + name)

    print("You only have " + str(health) + "max health")
    print("Adventure begins!")
    print(".")
    print(".")
    print(".")

    print("You went out of the village")


def place_of_power():
    global health
    print()
    print()
    print("You came into a Monolith of Place of Power!")
    power = input("Draw power from it? (yes/no): ")
    print()
    print()
    if power == "yes" or "Yes":
        print("Your max health increased into 15!")
        health = 15
        print("Remaining health: " + str(health))
    else:
        print("Max health didn't increase")



def cross():
    global health
    _3rd = input("You're now in a crossroads, which way to go? (left/right): ")
    if _3rd == "left":
        print()
        print("There is a wizard, and asks you a question.")
        print("If you got it right, he restores your health to full")
        print("If you got it wrong, he will kill you using magic!")
        print()
        print("The question: ")
        print()
        print("You are given 5 paper money worth of 20 each, you buy a food worth 47.")
        answer = input("How much is the change?:  ")
        if answer == "13":
            health = 10
            print("Health restored to max!")
            print("Remaining health: " + str(health))
        else:
            print("Wrong Answer!")
            print("You got killed by the wizard! You lose the game!")
            print()
            print()
            restart = input("Do you want to play again? (Yes/No): ")
            print()
            if restart == "yes" or restart == "Yes":
                start()
            else:
                exit()
    else:
        print()
        print("You fell into a hole! You lose the game!")
        print()
        print()
        restart = input("Do you want to play again? (Yes/No): ")
        print()
        if restart == "yes" or restart == "Yes":
            start()
        else:
            exit()


def long_way():
    global health
    print("You're traveling a long journey in a road")
    print(".")
    print(".")
    print(".")
    print("You got surrounded by bandits! You fought them. You lose 3 health!")
    health -= 3
    print("Remaining health: " + str(health))
    print(".")
    print(".")
    print(".")
    response = input("There are wolves! (fight/run): ")
    if response == "fight" or "Fight":
        print("You killed the wolves and you lose 3 health!")
        health -= 3
        print("Remaining health: " + str(health))
        place_of_power()
    elif response == "run" or "Run":
        print("You barely escaped!")
        place_of_power()

def suspicious_man():
    print()
    help = input("There is a suspicious man asking for help, help him? (yes/no): ")

    if help == "yes" and "Yes":
        print("You are rewarded a horse for helping the man!")
        print("You can now travel fast!")
        place_of_power()
    elif help == "no" and "No":
        print("You ignored him")
        print()
        long_way()


def left1():
    global health
    _2nd = input("You came into a lake, (swam across/go around): ")
    if _2nd == "swam across":
        print("You got bit by a fish! You lose 2 health")
        health -= 2
        print("Remaining health: " + str(health))
        print()

    hunt = input("You found a deer, hunt it? (yes/no): ")
    if hunt == "yes":
        print()
        print(" ")
        method = input("Hunting a deer - (Set a trap/Throw your sword/Chase it): ")

        if method == "set a trap" or "Set a trap":
            print(" You caught the deer! Made food\n health increased by 1!")
            if health < 10:
                health += 1
                print("Remaining health: " + str(health))
                suspicious_man()
            else:
                print("Still at max health: " + str(health))
                suspicious_man()
        elif method == "throw a sword" or "Throw a sword":
            print("You missed the deer!")
            suspicious_man()
        elif method == "Chase it" or "chase it":
            print("Didn't caught the deer, you got tired, you lose 1 health!")
            health -= 1
            print("Remaining health: " + str(health))
            suspicious_man()
    else:
        suspicious_man()


def right1():
    global health
    _2nd = input("You came into a dark forest. (go in/go another way): ")
    if _2nd == "go in":
        print("A monster showed up! You fought it! You lose 5 health!")
        health -= 5
        print("Remaining health: " + str(health))
        cross()

    elif _2nd == "go another way":
        print("You came into a bushes. You fought a pack of wolves! You lose 3 health!")
        health -= 3
        print("Remaining health: " + str(health))
        cross()


_1st = input("There are two paths, which way to go? (left/right): ")

while _1st != "left" and _1st != "right":
    print("Enter the correct path!")
    _1st = input("There are two paths, which way to go? (left/right): ")

if _1st == "left":
    left1()

if _1st == "right":
    right1()
