h = int(input())
y = int(input())
x = int(input())

x1 = 4*h
y1 = h
x2 = h
y2 = 2 * h
x3 = h
y3 = 0
x4 = 0
y4 = 3 * h

if (x <= x1 and x >= x2 and y >= y1 and y <= y2) or (x <= x3 and x >= x4 and y >= y3 and y <= y4):
    if (((x == x1 or x == x2) and y >= y1 and y <= y2) or ((y == y1 or y == y2) and x <= x1 and x >= x2) or
            ((x == x3 or x == x4) and y >= y3 and y <= y4) or ((y == y3 or y == y4) and x <= x3 and x >= x4)):
        if (y > y1 and y < y2) and (x == x2 or x == x3):
            print("inside")
        else:
            print("border")
    else:
        print("inside")
else:
    print("outside")