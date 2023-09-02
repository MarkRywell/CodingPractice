
def cal():
    num1 = int(input("Enter a number: "))
    op = input()
    num2 = int(input("Enter a number: "))
    result = 0

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*' or op == 'x':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2

    print(round(result, 2))
    print("")
    again = input("Compute Again? Y/N:  ")

    if again == "Y":
        cal()
    elif again == "N":
        return 0

cal()

