import math

numbers = list(map(float,input().split(' ')))
for i in numbers:
    if i >=0:
        numbers_round =  math.trunc(abs(i)+0.5)
    else:
        numbers_round = math.trunc(i-0.5)

    print("{0} => {1} ".format(i,numbers_round))