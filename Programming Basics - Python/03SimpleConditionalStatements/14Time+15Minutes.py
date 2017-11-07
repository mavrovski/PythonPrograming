hour=int(input())
minutes=int(input())
sumInMinutes=hour*60+minutes
sumPlus15Minutes = sumInMinutes+15
newHour = int(sumPlus15Minutes/60)
newMinutes = sumPlus15Minutes%60

if newHour>=24:
    newHour = 0
    if newMinutes <= 9:
        print("{0}:0{1}".format(newHour,newMinutes))
    else:
        print("{0}:{1}".format(newHour, newMinutes))
else:
    if newMinutes <= 9:
        print("{0}:0{1}".format(newHour,newMinutes))
    else:
        print("{0}:{1}".format(newHour, newMinutes))


