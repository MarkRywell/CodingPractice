money = int(input("Enter an amount: "))

while money < 1000 or money > 100000:
    money = int(input("Please Enter a Valid amount: "))

months = int(input("Please Enter number of months: "))

while months < 1 or months > 12:
    months = int(input("Please Enter valid number of months: "))

print("Term of Payment            Interest")
print("[M]-onthly                  2%")
print("[Q]-uarterly                %7")
print("[A]-nnual                   %30")

interest = 0
final = 0
TOP = input("Enter Term of Payment: ")

if TOP == 'M':
    interest = money * 0.02 * (months/12)
    final = money + interest

    print("Money Amount:" + str(money))
    print("Number of months: " + str(months))
    print("Monthly Payment")
    print("Interest: " + str(interest))
elif TOP == 'Q':
    interest = money * 0.07 * (months/12)
    final = money + interest

    print("Money Amount:" + str(money))
    print("Number of months: " + str(months))
    print("Quarterly Payment")
    print("Interest: " + str(interest))
elif TOP == 'A':
    interest = money * 0.3 * (months/12)
    final = money + interest

    print("Money Amount:" + str(money))
    print("Number of months: " + str(months))
    print("Annual Payment")
    print("Interest: " + str(interest))

terminate = input("Do you wish to [T]ry again or [E]xit?: ")



