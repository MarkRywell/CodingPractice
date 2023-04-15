
def factorial(n):
    if n == 1: return 1
    else:
        return n * factorial(n - 1)



def factorial1(n):
    result = 1
    if n == 1: return 1
    else:
        for i in range(1, n+1):
            result *= i
        return result


def printHello(n):
    if n == 0: return
    else:
        print("Hello world")
        printHello(n-1)


def reverseWord(word):
    if len(word) == 0: return word
    else:

        return reverseWord(word[1:]) + word[0]


print(reverseWord("wtf"))



word = "hello"

list = list(word)
reverseList = []




