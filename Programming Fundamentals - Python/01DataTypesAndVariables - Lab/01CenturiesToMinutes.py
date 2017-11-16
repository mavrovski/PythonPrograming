centuries = int(input())
years = centuries *100
days = int(years*365.2422)
hours = 24* days
minutes = 60*hours

print("{0} centuries = {1} years = {2} days = {3} hours = {4} minutes".format(centuries,years,days,hours,minutes))