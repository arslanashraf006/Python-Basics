#A decorator is essentially a function that takes another function as an argument.
#functions are first class objects in python. What it means is that they can be treated  just like any other variable and you can pass them as argument to another function or even return them as return value
import time

# python allows you to write nested functions
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took "+str((end-start)*1000)+" mil sec")
        return result
    return wrapper

@time_it # decorate the function
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1, 100000)
calc_square(array)
calc_cube(array)