import math


def triangle_rectangle_area(figure,a,b):
    result = 0.0
    if figure == "triangle":
        result = (a*b)/2
    elif figure == "rectangle":
        result = a*b
    return result

def circle_square(figure,a):
    if figure == "circle":
        return math.pi*pow(a,2)
    elif figure == "square":
        return a*a

figure = input()
if figure == "triangle" or figure == "rectangle":
    a = float(input())
    b = float(input())
    print("%.2f" % triangle_rectangle_area(figure,a,b))
elif figure == "circle" or figure == "square":
    a = float(input())
    print("%.2f" % circle_square(figure,a))