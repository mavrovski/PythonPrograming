examHour = int(input())
examMinutes = int(input())
arriveHour = int(input())
arriveMinutes = int(input())

examTime = int(examHour*60+examMinutes)
arriveTime = int(arriveHour*60+arriveMinutes)
minutesDiff =  int(arriveTime-examTime)
if minutesDiff < -30:
    print("Early")
elif minutesDiff <= 0:
    print("On time")
else:
    print("Late")

if minutesDiff != 0:
    hour = abs(int(minutesDiff/60))
    minutes = abs(minutesDiff)%60
    if hour>0:
        if minutes < 10:
            print("{0}:0{1} hours".format(hour,minutes),end='')
        else:
            print("{0}:{1} hours".format(hour, minutes),end='')
    else:
        print(str(minutes)+" minutes",end='')
    if minutesDiff<0:
        print(" before the start")
    else:
        print(" after the start")