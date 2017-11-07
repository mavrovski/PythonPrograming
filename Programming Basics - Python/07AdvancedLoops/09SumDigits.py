n = int(input())
num = 0
while n != 0:
    num+=int(n%10)
    n/=10
print(num)