class Animal:
    def __init__(self, habitat):
        self.habit = habitat

    def print_habit(self):
        print(self.habit)

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("woof woof")

x = Dog()
x.print_habit()
x.sound()