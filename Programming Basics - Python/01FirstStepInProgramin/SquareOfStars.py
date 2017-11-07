numbersOfStars = int(input())
topAndBottomSide = '*'*numbersOfStars
print(topAndBottomSide)
for i in range (1,numbersOfStars-1):
    print('*',end = '')
    print(' ' * (numbersOfStars-2),end='')
    print('*')
print(topAndBottomSide)
