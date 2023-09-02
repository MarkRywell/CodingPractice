class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Students(Person):
    def __init__(self, name, age, grade):
        self.grade = grade


class Teachers(Person):
    def __init__(self, name, age, subject):

        self.subject = subject

