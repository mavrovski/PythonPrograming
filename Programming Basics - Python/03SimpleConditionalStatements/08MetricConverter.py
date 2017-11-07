metric = float(input())
fromMeters = input()
toMeters = input()
result = 0.0
metricToMeeter = 0.0
if fromMeters == "m":
    metricToMeeter = metric
if fromMeters == "mm":
    metricToMeeter = metric / 1000
if fromMeters == "cm":
    metricToMeeter = metric / 100
if fromMeters == "mi":
    metricToMeeter = metric / 0.000621371192
if fromMeters == "in":
    metricToMeeter = metric / 39.3700787
if fromMeters == "km":
    metricToMeeter = metric / 0.001
if fromMeters == "ft":
    metricToMeeter = metric / 3.2808399
if fromMeters == "yd":
    metricToMeeter = metric / 1.0936133

if toMeters == "m":
    result = metricToMeeter
if toMeters == "mm":
    result = metricToMeeter * 1000
if toMeters == "cm":
    result = metricToMeeter * 100
if toMeters == "mi":
    result = metricToMeeter * 0.000621371192
if toMeters == "in":
    result = metricToMeeter * 39.3700787
if toMeters == "km":
    result = metricToMeeter * 0.001
if toMeters == "ft":
    result = metricToMeeter * 3.2808399
if toMeters == "yd":
    result = metricToMeeter * 1.0936133



print("{0} {1}".format(result,toMeters))