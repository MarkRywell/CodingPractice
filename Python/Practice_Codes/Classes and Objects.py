class Awaken:
    def __init__(self, name, strength, height):
        self.name = name
        self.strength = strength
        self.height = height

    def introduce(intro):
        print("My name is " + intro.name)
        print("And I'm " + intro.strength + "!")

    def show_height(spec):
        print("I am " + str(spec.height) + "cm tall.")


p1 = Awaken("Kaiden", "Strong", 170)
p2 = Awaken("Jiwoo", "Moderate", 160)
p1.strength = "Overpowered"


p1.introduce()
p2.introduce()

p1.show_height()