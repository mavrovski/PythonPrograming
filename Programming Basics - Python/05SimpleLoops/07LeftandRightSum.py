n = int(input())
leftSum = 0
rightSum = 0

for i in range(0,n):
    leftSum+=int(input())
for j in range(0,n):
    rightSum+=int(input())

if abs(leftSum-rightSum) == 0:
    print("Yes, sum = {0}".format(abs(leftSum)))
else:
    print("No, diff = {0}".format(abs(leftSum-rightSum)))

