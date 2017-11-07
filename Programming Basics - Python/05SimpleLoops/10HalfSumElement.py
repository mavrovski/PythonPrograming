n = int(input())
numbers = []
maxNumber = 0
currentSum = 0
for i in range(0,n):
    numbers.append(int(input()))
    maxNumber = max(numbers[i],maxNumber)
    currentSum+=numbers[i]
currentSum -= maxNumber
if maxNumber == currentSum:
    print("Yes \nSum = {0}".format(maxNumber))
else:
    print("No \nDiff = {0}".format(abs(maxNumber-currentSum)))