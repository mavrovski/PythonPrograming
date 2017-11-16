import math


def cube_properties(side,property):
    result = 0.0
    if property == "face":
        result = math.sqrt(2 * (side ** 2))
    elif property == "space":
        result = math.sqrt(3 * (side ** 2))
    elif property == "volume":
        result = side ** 3
    elif property == "area":
       result = 6*(side**2)
    return result

side = float(input())
property = input().lower()
print("{0:.2f}".format(cube_properties(side,property)))