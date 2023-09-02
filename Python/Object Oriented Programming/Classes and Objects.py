class Cars:
    def __init__(self, color, speed, transmission):
        self.color = color
        self.speed = speed
        self.transmission = transmission

    def introduce(intro):
        print("Color:", intro.color, "\nTransmission:", intro.transmission)

    def change_transmission(gear):

        if gear.transmission == 'Automatic':
            gear.transmission = 'Manual'
        else:
            gear.transmission = 'Automatic'

        return gear.transmission


c1 = Cars('Red', 200, 'Manual')


c1.introduce()


