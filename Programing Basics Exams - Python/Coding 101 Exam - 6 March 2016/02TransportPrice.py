km = float(input())
dayOrNight = input().lower()

totalPrice = 0.0
taxiStartPrice = 0.70
busPrice = 0.09
trainPrice = 0.06
busTotalPrice = 0.0
trainTotalPrice = 0.0
if dayOrNight == "day":
    taxiPrice = 0.79
    if km <= 20:
        totalPrice = taxiStartPrice+(taxiPrice*km)
    if km >= 20:
        busTotalPrice = busPrice*km
        totalPrice = busTotalPrice
    if km >=100:
        trainTotalPrice = trainPrice*km
        totalPrice = trainTotalPrice
        if trainTotalPrice < busTotalPrice:
            totalPrice = trainTotalPrice

    print("{0:g}".format(totalPrice))

elif dayOrNight == "night":
    taxiPrice = 0.90
    if km <= 20:
        totalPrice = taxiStartPrice + (taxiPrice * km)
    if km >= 20:
        busTotalPrice = busPrice * km
        totalPrice = busTotalPrice
    if km >= 100:
        trainTotalPrice = trainPrice * km
        totalPrice = trainTotalPrice
        if trainTotalPrice<busTotalPrice:
            totalPrice = trainTotalPrice

    print("{0:g}".format(totalPrice))