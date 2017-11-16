from _decimal import Decimal


def calculate_center_point(x1,y1,x2,y2):
    if (x1**2)+(y1**2)>=(x2**2)+(y2**2):
        print("({0:g}, {1:g})".format(x2, y2))
    else:
        print("({0:g}, {1:g})".format(x1, y1))


x1 =Decimal(input())
y1 = Decimal(input())
x2 = Decimal(input())
y2 = Decimal(input())

calculate_center_point(x1,y1,x2,y2)