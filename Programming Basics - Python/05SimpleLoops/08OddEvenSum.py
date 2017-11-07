n = int(input())
oddSum = 0
evenSum = 0

for i in range(0,n):
    if i % 2 == 0:
        evenSum+=int(input())
    else:
        oddSum += int(input())
if abs(oddSum-evenSum) == 0:
    print("Yes \nSum = {0}".format(abs(evenSum)))
else:
    print("No \nDiff = {0}".format(abs(oddSum-evenSum)))
