n = int(input())
l = int(input())

for firstDigit in  range (1,n+1):
    for secondDigit in range(1,n+1):
        for firstLetter in  range (97,97+l):
            for secondLetter in range(97,97+l):
                for thirdDigit in range(1, n+1):
                    if thirdDigit>firstDigit and thirdDigit>secondDigit:
                        print("{0}{1}{2}{3}{4}".format(firstDigit,secondDigit,chr(firstLetter),chr(secondLetter),thirdDigit),end=' ')


