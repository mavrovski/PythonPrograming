n =  int(input())
num = 1
for rows in range(1,n+1):
    for col in range (1,rows+1) :
        if col>=1:
            print("{0} ".format(num),end='')
            num+=1
        if num>n:
            break
    print()
    if num > n:
        break