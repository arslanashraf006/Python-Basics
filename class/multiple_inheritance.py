class Father:
    def gardening(self):
        print("I enjoy gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def sport(self):
        print("I enjoy sports")

c = Child()
c.gardening()
c.cooking()
c.sport()

class Father:
    def skills(self):
        print("gardening, programming")

class Mother:
    def skills(self):
        print("cooking, art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()