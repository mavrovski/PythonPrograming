centuries = int(input())
years = int(centuries *100)
days = int(years*365.2422)
hours = int(days*24)
minutes = int(hours*60)
seconds = int(minutes*60)
milliseconds = int(seconds*1000)
microseconds = int(milliseconds*1000)
nanoseconds = int(microseconds*1000)

print("{0} centuries = {1} years = {2} days = {3} hours = {4} minutes = {5} seconds = {6} milliseconds = {7} microseconds = {8} nanoseconds"
      .format(centuries,years,days,hours,minutes,seconds,milliseconds,microseconds,nanoseconds))


