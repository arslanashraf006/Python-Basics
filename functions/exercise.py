#1

def calculate_area(base, height):
    area = (1/2)*base*height
    return area

a = calculate_area(10, 20)
print("Area of triangle is ", a)

#2

def calculate_area(base, height, shape = 'triagnle'):
    area = 0
    if shape == "triagnle":
        area = (1/2)*base*height
    elif shape == "rectangle":
        area=height*base
    return area
#It can be either "triangle" or "rectangle"
b = calculate_area(10, 20, "rectangle")
print("Area is ", b)

#3

def print_pattern(num):
    for i in range(1, num+1):
        print("*" * i)

print_pattern(4)