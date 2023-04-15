
def life():
    print("You woke up early")

    hungry = input("Are you hungry?: Yes or No: ")

    if hungry == "Yes":
        print("Then eat breakfast!")
    elif hungry == "No":
        print("Then don't")

    print()

    print("You're leaving your house")

    weather = input("Is it cloudy or sunny?: ")

    if weather == "cloudy":
        print("Bring an umbrella")
    elif weather == "sunny":
        print("Bring sunglasses")

    print()

    print("You're at a restaurant")

    food = input("Do you want meat or pasta or salad?: ")

    if food == "meat":
        print("Order a steak")
    elif food == "pasta":
        print("Order spaghetti & meatballs")
    elif food == "salad":
        print("Order a salad")
    else:
        print("Order the fuck you want!")



def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

max = max_num(24, 12, 20)

print(max)