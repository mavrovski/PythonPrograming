n = int(input())

result = 0
isSpecial = bool(False)
for i in range(1,n+1):
    num = int(i)
    result = int(0)
    while num>0:
        result += int(num % 10)
        num /= int(10)
        isSpecial = result == 5 or result == 7 or result == 11

    print("{0} -> {1}".format(i,isSpecial))