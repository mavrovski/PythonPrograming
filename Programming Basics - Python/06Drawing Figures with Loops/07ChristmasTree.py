n = int(input())


for row in range(0,n+1):
    stars = "*"*row
    space = " "*(n-row)
    print(space ,end='')
    print(stars, end='')
    print(" | ",end='')
    print(stars, end='')
    print(space, end='')
    print()

