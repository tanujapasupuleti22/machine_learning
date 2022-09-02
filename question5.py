import math

# defining area and circumference functions
# using math.pi to get pi value.
def area(radius):
    return math.pi * radius * radius

def circum(radius):
    return 2 * math.pi * radius

radius = 30;
# calculating the area of circle using formula pi*r**2
_area_of_circle_ = area(radius)
print("Area of circle: " + str(_area_of_circle_))

# calculating the circumference of circle using formula 2*pi*r
_circum_of_circle_ = circum(radius)
print("Circumference of circle: " + str(_circum_of_circle_))

# taking radius as user input using input() function and calculating the area.
print("Enter radius to calculate area: ")
user_input = int(input())
print("Area of user input radius: " + str(area(user_input)))