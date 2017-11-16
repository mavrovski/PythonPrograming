n = int(input())

for firstLetter in range(ord('a'), ord('a') + n):
    for secondLetter in range(ord('a'), ord('a') + n):
        for thirdLetter in range(ord('a'), ord('a') + n):
            print("{0}{1}{2}".format(chr(firstLetter),chr(secondLetter),chr(thirdLetter)))

