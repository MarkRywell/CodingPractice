# Problem 3
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
    greet = "Hello " + name + "!"
    return greet


print(hello_name(input("Enter name: ")))
