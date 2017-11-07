n = int(input())
number = 0
currentMaxNumber = 0
for i in range(0,n):
    number=int(input())
    if number<currentMaxNumber:
        currentMaxNumber = number
    if i == 0:
        currentMaxNumber = number
print(currentMaxNumber)
