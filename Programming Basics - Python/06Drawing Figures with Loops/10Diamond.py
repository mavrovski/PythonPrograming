n = int(input())

leftRightDashes = int((n-1)/2)


if n == 1:
    print("*")
else:
    # upside
    for row in range(0,int((n-1)/2)):
        print("-"*leftRightDashes,end='')
        print("*",end='')
        middle = int(n - 2 * leftRightDashes - 2)
        if middle >= 0:
            print("-" * middle, end='')
            print("*", end='')
        print("-" * leftRightDashes)
        leftRightDashes-=1

    print("*"+"-"*(n-2)+"*")
    leftRightDashes+=1
    # downside
    for downRow in range(0,int((n-1)/2)):
        print("-"*leftRightDashes,end='')
        middle = int(n - 2 * leftRightDashes - 2)
        print("*",end='')
        if middle >= 0:
            print("-" * middle, end='')
            print("*", end='')
        print("-" * leftRightDashes)
        leftRightDashes += 1
