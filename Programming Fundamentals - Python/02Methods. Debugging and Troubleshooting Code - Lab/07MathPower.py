import math
from _decimal import Decimal

number = Decimal(input())
power = int(input())


def raise_to_power(number, power):
    return Decimal(number**power)


result = raise_to_power(number,power)
print(result)
