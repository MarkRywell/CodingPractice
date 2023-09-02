class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


class Manager(Person):
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position
        self.employees = []

    def introduce(self):
        print(f"Hello! I'm {self.name} and I'm the {self.position}.")

    def hire_employee(self, employee):
        self.employees.append(employee)
        return True


class Employee(Person):
    def __init__(self, name, age, gender, work):
        super().__init__(name, age, gender)
        self.work = work

    def introduce(self):
        print(f"Hi! I'm {self.name} and I do the {self.work}.")




manager1 = Manager("Brian", 38, "Male", "Chief Technical Officer")
manager1.introduce()

employee1 = Employee("John", 25, "Male", "Software development")
employee1.introduce()

