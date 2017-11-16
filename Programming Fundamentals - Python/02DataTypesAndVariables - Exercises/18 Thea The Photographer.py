import math
import time
picturesCounts = int(input())
filterTime = int(input())
filterFactor = int(input())
uploadTime = int(input())

filteredPictures = int(math.ceil(float(picturesCounts*(filterFactor/100))))

totalTime = int(filteredPictures*uploadTime+int(picturesCounts)*filterTime)
totalDays = int(totalTime / (24*3600))


day = int(totalTime / (24 * 3600))
totalTime = int(totalTime % (24 * 3600))
hour = int(totalTime / 3600)
totalTime %= int(3600)
minutes = (totalTime / 60)
totalTime %= int(60)
seconds = totalTime
print("%d:%.2d:%2d:%.2d" % (day, hour, minutes, seconds))

# print("{0}:{1}".format(totalDays,time.strftime("%H:%M:%S" , time.gmtime(totalTime))))
