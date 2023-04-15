# Problem 13
# Make a class with a function that divides a user's input
# with a value that is predefined in the class (not in the function.)


class Divide:

    def __init__(self, number):
        self.number = number

    def divide(self):
        quotient = self.number / 4

        return quotient


num1 = Divide(20)

print(num1.divide())