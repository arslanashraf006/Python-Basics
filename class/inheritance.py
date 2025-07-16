class Vehical:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehical):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific uage: commute to work, vacation with family")

class MotorCycle(Vehical):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific uage: road trip, racing")

c = Car()
c.general_usage()
c.specific_usage()


m = MotorCycle()
m.specific_usage()
#Built-in method, tells instance is object of specific class
print(isinstance(c, Car))

#Built-in method, tell car is subclass of vehical
print(issubclass(Car, Vehical))