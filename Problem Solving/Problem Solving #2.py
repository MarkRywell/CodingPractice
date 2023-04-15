# Problem 2
# Given a string and a non-negative, return a larger string that original string.

def larger_string(string, number):
    large = string * number
    return large


print(larger_string("Krishia", 10))