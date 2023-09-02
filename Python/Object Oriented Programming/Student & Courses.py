
class Students:

    # Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade   # 0 - 100

    # Methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def get_course_max(self):
        return self.name, self.max_students

    def get_current(self):
        return len(self.students)

    def add_student(self, student):
        self.student = student

        if len(self.students) < self.max_students:
            self.students.append(student)
            return True

        return False

    def get_average(self):
        value = 0

        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)




course1 = Course("IT", 3)
print(course1.get_course_max())

student1 = Students("Mark", 20, 95)
student2 = Students("Wincy", 20, 93)
student3 = Students("CJ", 18, 97)
student4 = Students("Luces", 18, 96)


print(course1.add_student(student1))
print(course1.add_student(student2))
print(course1.add_student(student3))

print(course1.get_current())

print(course1.get_average())

