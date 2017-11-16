from _decimal import Decimal

width = Decimal(input())
height = Decimal(input())


def get_triangle_area(width, height):
    return Decimal(width*height/2)


area = get_triangle_area(width,height)

print(area)