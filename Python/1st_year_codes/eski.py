word = "yes"

while(word == "yes"):
    number1 = input("Pag butang og number boss: ")
    number2 = input("Isa pa ka number boss: ")

    while (not number1.isnumeric() or not number2.isnumeric()):
        print("Dili puwede")
        number1 = input("Pag butang og number boss: ")
        number2 = input("Isa pa ka number boss: ")

    num1 = float(number1)
    num2 = float(number2)

    operation = input("Butang sa imong gusto nga operation boss (+, -, *, /): ")


    if (operation == "+"):
        num3 = num1 + num2
        print(num3)
        print("okeh kayo")

    elif (operation == "-"):
        num3 = num1 - num2
        print(num3)
        print("okeh kayo")

    elif (operation == "*"):
        num3 = num1 * num2
        print(num3)
        print("okeh kayo")

    elif (operation == "/"):
        num3 = num1 / num2
        print(num3)
        print("okeh kayo")

    else:
        print("hubog man guro ka boss?")
        print("relax sa")

    word = input("mo utro paka boss? yes or no: ")

print("grabika batak")
print("brayt na kayo ka")