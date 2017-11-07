n = int(input())


oddSum = 0
oddMin = 1000000000.0
oddMax = -1000000000.0

evenSum = 0
evenMin =  1000000000.0
evenMax = -1000000000.0
for i in range (1,n+1):
    number = float(input())
    if i % 2 ==0:
        evenSum += number
        if number>evenMax:
            evenMax = number
        if number<evenMin:
            evenMin = number
    else:
        oddSum+=number
        if number>oddMax:
            oddMax = number
        if number<oddMin:
            oddMin = number

if evenMax == -1000000000.0:
    evenMax = 0

if evenMin == 1000000000.0:
    evenMin = 0
if oddMin == 1000000000.0:
    oddMin = 0

if oddMax == -1000000000.0:
    oddMax = 0

i

if n == 1:
    print("OddSum=%g," % oddSum)
    print("OddMin=%g," % oddMin)
    print("OddMax=%g," % oddMax)
    print("EvenSum=%g,"% evenSum)
    print("EvenMin=No,")
    print("EvenMax=No")
elif n == 0:
    print("OddSum=%g," % oddSum)
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=%g," % evenSum)
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print("OddSum=%g," % oddSum)
    print("OddMin=%g," % oddMin)
    print("OddMax=%g," % oddMax)
    print("EvenSum=%g," % evenSum)
    print("EvenMin=%g," % evenMin)
    print("EvenMax=%g" % evenMax)



