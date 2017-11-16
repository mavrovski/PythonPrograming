from _decimal import Decimal

distanceInMeters = float(input())
hours = float(input())
minutes = float(input())
seconds = float(input())

totalTimeInSeconds = float(hours*60*60+minutes*60+seconds)

metersPerSecond = float(distanceInMeters/totalTimeInSeconds)
kmPerHours = float(metersPerSecond)*float(3.60)
milesPerHours = float(kmPerHours)/float(1.609)

print("{0:.6f}" .format(metersPerSecond) )
print("{0:.6f}" .format(kmPerHours) )
print("{0:.6f}" .format(milesPerHours))
