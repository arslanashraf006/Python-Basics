class Employee:
    def __init__(self, i, n):
        self.id = i
        self.name = n
    
    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating a emp instance of Employee class
emp = Employee(1, "coder")

emp.display()
# Deleting the property of object
del emp.id
# Deleting the object itself
try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")