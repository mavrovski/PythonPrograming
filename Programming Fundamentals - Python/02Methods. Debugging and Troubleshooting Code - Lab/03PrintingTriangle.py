def print_line(start,end):
    for i in range(start,end+1):
        print("{0} ".format(i),end='')
    print()

n = int(input())
for i in range(0,n):
    print_line(1,i)

print_line(1,n)

for i in range(n-1,-1,-1):
    print_line(1,i)
