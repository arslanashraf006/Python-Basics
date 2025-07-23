class Teacher:
    def teachers_action(self):
        print("I can teach")

class Engineer:
    def engineers_action(self):
        print("I can code and teach")

class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")

class Person(Teacher, Engineer, Youtuber):
    pass

coder = Person()
coder.teachers_action()
coder.engineers_action()
coder.youtubers_action()