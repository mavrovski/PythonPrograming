n = int(input())

p1 = 0.0
p2 = 0.0
p3 = 0.0
p4 = 0.0
p5 = 0.0
num = int
for i in range(0,n):
    num = int(input())
    if num < 200:
        p1+=1
    elif num >= 200 and num <400:
        p2 += 1
    elif num >= 400 and num < 600:
        p3 += 1
    elif num >= 600 and num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1
print("{0:.2f}%".format((p1/n)*100))
print("{0:.2f}%".format((p2/n)*100))
print("{0:.2f}%".format((p3/n)*100))
print("{0:.2f}%".format((p4/n)*100))
print("{0:.2f}%".format((p5/n)*100))