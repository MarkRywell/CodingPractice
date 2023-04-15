# Problem 5
# Give na string, return a string where for every char in the original, there are two chars.

def double_char(str):
    to_return = ""

    for letter in str:
        to_return += letter * 2

    return to_return


print(double_char('krishia-panda'))