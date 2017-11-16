import math

x1 =float(input())
y1 =float(input())
x2 =float(input())
y2 =float(input())

x3 =float(input())
y3 =float(input())
x4 =float(input())
y4 =float(input())


def line_length(x1, y1, x2, y2):
    difference_between_x = abs(x1-x2)
    difference_between_y = abs(y1-y2)
    line = math.sqrt(pow(difference_between_x,2)+pow(difference_between_y,2))
    return line

def closest_point_to_center(x1,y1,x2,y2):
    if pow(x1,2)+pow(y1,2)<=pow(x2,2)+pow(y2,2):
        coordinates = "({0:g}, {1:g})({2:g}, {3:g})".format(x1,y1,x2,y2)
    else:
        coordinates = "({0:g}, {1:g})({2:g}, {3:g})".format(x2, y2, x1, y1)
    return coordinates



line_of_first_pair = line_length(x1,y1,x2,y2)
line_of_second_pair = line_length(x3,y3,x4,y4)
result = ""
if line_of_first_pair>=line_of_second_pair:
    result = closest_point_to_center(x1,y1,x2,y2)
    print(result)
else:
    result = closest_point_to_center(x3, y3, x4, y4)
    print(result)
