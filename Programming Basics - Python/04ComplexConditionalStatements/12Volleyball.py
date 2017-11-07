import math

typeOfyear = input().lower()
holidays = float(input())
weekendsToHome  = float(input())
weekendsInYear = 48
weekendsInSofia = weekendsInYear - weekendsToHome
gamesInSofia = (weekendsInSofia * 3)/4
gamesInHome = weekendsToHome
gamesInHolidays = (holidays*2)/3
totalGames = gamesInSofia+gamesInHome+gamesInHolidays

if typeOfyear == "leap":
    totalGames = totalGames+totalGames*0.15
    print(math.floor(totalGames))
elif typeOfyear == "normal":
    print(math.floor(totalGames))