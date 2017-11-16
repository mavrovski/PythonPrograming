from _decimal import *
import math

n = int(input())
result = 0
for i in range(0,n):
    num = input()
    result += Decimal(num)
    # result += Decimal(i)+Decimal(i+1)
print(result)
