# Problem 11
# Write a function 'maskify', which changes all but the last four into '#'


def maskify(cc):
    new_cc = ""

    for letter in cc:
        if letter == cc[-4]:
            new_cc += letter
        else:
            new_cc = new_cc + "#"

    return new_cc

print(maskify("12345678"))