n = int(input())

topAndBottomSide = "*"*(n*2)+" "*(n)+"*"*(n*2)
middlePart = "*"+"/"*(2*n-2)+"*"+" "*(n)+"*"+"/"*(2*n-2)+"*"
middlePartLine = "*"+"/"*(2*n-2)+"*"+"|"*(n)+"*"+"/"*(2*n-2)+"*"
print(topAndBottomSide)
for i in range(0,n-2):
    if i == int((n-1)/2-1):
        print(middlePartLine)
    else:
        print(middlePart)

print(topAndBottomSide)