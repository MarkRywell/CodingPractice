class Robot:
    def __init__(robot, name, color, weight):
        robot.name = name
        robot.color = color
        robot.weight = weight

    def introduceSelf(intro):
        print("My name is " + intro.name)


r1 = Robot("Mark", "blue", 65)
r2 = Robot("Krishia", "green", 50)


class Person:
    def __init__(person, name, personality, isSitting, robotOwned):
        person.name = name
        person.personality = personality
        person.isSitting = isSitting
        person.robotOwned = robotOwned

    def sitDown(self):

        self.isSitting = True

    def standUp(self):

        self.isSitting = False


p1 = Person("Alice", "aggressive", False, r2)
p2 = Person("Becky", "talkative", True, r1)


p1.robotOwned.introduceSelf()
p2.robotOwned.introduceSelf()
