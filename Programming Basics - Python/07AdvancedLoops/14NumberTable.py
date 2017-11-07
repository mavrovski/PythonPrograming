n = int(input())

for rows in range(0,n):
    for cols in range(0,n):
        num  = rows+cols+1
        if num>n:
            num = 2*n-num
        print("{0} ".format(num),end='')
    print()