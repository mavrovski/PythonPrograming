number = int(input())
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

if  number==1 or number == 2 or number == 3 or number ==4 or number == 5 or number == 6 or number ==7:
    for i in range(0, len(days)):
         if i + 1 == number:
             print(days[i])
else:
    print("Error")
