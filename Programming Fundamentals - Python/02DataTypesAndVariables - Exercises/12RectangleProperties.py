import math

width = float(input())
height = float(input())

area = width*height
perimeter = width*2+height*2
diagonal = math.sqrt(pow(width,2)+pow(height,2))

print("{0:.15g}".format(perimeter))
print("{0:.15g}".format(area))
print("{0:.15g}".format(diagonal))