x = 1

while x <= 100:
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")

    elif x % 3 == 0:
        print("Fizz")

    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x = x + 1

# for i in range(100):
#     print(i)