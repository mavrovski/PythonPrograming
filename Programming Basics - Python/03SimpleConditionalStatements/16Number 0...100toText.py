number = int(input())
numbersToNineteen = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
                     'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
numbersToNinety = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']


if number <0 :
    print('invalid number')
elif number>100:
    print('invalid number')
elif number>=0 and number<20:
    print(numbersToNineteen[number])
elif number>=20 and number < 100:
    indexToHundred = int((number/10)-2)
    indexToTen=(number%10)
    if number%10 == 0:
        print("{0}".format(numbersToNinety[indexToHundred]))
    else:
        print("{0} {1}".format(numbersToNinety[indexToHundred],numbersToNineteen[indexToTen]))
elif number == 100:
    print('one hundred')