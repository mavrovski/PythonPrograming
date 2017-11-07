import math

figure = input()

if figure == "square":
    side = float(input())
    print("{0:.3f}".format(side*side))
elif figure == "circle":
    radius = float(input())
    print("{0:.3f}".format(math.pi*(radius*radius)))
elif figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    print("{0:.3f}".format(sideA*sideB))
elif figure == "triangle":
    sideA = float(input())
    sideH = float(input())
    print("{0:.3f}".format(sideA*sideH/2))
# (square, rectangle, circle или triangle).