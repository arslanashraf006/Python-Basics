#3

import math

def circle_calc():
    radius = float(input("Enter radius of the circle: "))

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

# Main program
area, circumference, diameter = circle_calc()

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Diameter: {diameter:.2f}")
