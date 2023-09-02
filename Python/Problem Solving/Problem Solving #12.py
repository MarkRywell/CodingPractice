# Problem 12
# Greet a happy birthday according to the person's birthdate

from datetime import *

today = date.today()

def greet(name, year, month, day):

    birthdate1 = date(year, month, day)

    if birthdate1 == today:
        print("Happy Birthday " + name + "!")
    elif birthdate1 > today:
        print('Advance Happy Birthday ' + name + "!")
    else:
        print('Belated Happy Birthday ' + name + "!")

greet("Mark", 2001, 8, 16)