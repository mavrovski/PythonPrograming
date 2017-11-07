n = int(input())
valueOne = 0.0
valueTwo = 0.0
pairSum = 0.0
oldPairSum = 0.0
diff = 0.0
maxDiff = 0.0

for i in range(0,n) :
    valueOne = float(input())
    valueTwo = float(input())
    if i == 0:
        oldPairSum = valueOne+valueTwo
    else:
        pairSum = valueOne+valueTwo
        diff = abs(pairSum-oldPairSum)
        if diff >maxDiff:
            maxDiff = diff
        oldPairSum = pairSum

if maxDiff == 0:
    print("Yes, value={0:g}".format(oldPairSum))
else:
    print("No, maxdiff={0:g}".format(maxDiff))