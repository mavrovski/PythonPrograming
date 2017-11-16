numOne = float(input())
numTwo = float(input())

eps = float(0.000001)
isTrue = (abs(numOne-numTwo)<eps)
print(isTrue)