playerOneSeconds = int(input())
playerTwoSeconds = int(input())
playerThreeSeconds = int(input())

sumOfSeconds = playerOneSeconds+playerTwoSeconds+playerThreeSeconds
minutes = int(sumOfSeconds/60)
seconds = sumOfSeconds%60
if seconds<=9:
    print("{0}:0{1}".format(minutes,seconds))
else:
    print("{0}:{1}".format(minutes, seconds))