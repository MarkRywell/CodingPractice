name1 = "Ralph"
science1 = 90
math1 = 88

name2 = "Lloyd"
science2 = 92
math2 = 92

name3 = "Andre"
science3 = 92
math3 = 90

name4 = "CJ"
science4 = 95
math4 = 96


def function1(name, science, math):
    intelligence = (science + math) / 2
    print("Intelligence Level: ")
    print(intelligence)
    if intelligence > 90:
        return name + " is smart."
    else:
        return name + " isn't smart"


result1 = function1(name1, science1, math1)
result2 = function1(name2, science2, math2)
result3 = function1(name3, science3, math3)
result4 = function1(name4, science4, math4)

print(result1)
print(result2)
print(result3)
print(result4)

