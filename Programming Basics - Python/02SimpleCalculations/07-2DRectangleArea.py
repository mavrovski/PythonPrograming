x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())

sideA = max(x1,x2)-min(x1,x2)
sideB = max(y1,y2)-min(y1,y2)

area = sideA*sideB
peimeter = 2*(sideA+sideB)

print(area)
print(peimeter)
