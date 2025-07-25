class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception:", self.msg)

    def handle(self):
        print("accident occured. take detour!")

try:
    raise Accident("crash between two class")
except Accident as e:
    e.print_exception()
    e.handle()