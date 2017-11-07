n = int(input())

# top side
for row in range(1,n+1):
    print(" "*(n-row),end='')
    print("*",end='')
    print(" *"*(row-1), end='')
    print()

# bottom side
for row in range(n-1,0,-1):
    for col in range(n-row,0,-1):
        print(" ", end='')
    for col in range(1,row+1):
        print("* ", end='')

    print()