num = int(input())
scores=0.0
if num<=100:
    scores+=5
elif num>100 and num<=1000:
    scores+=num*0.2
elif num>1000:
    scores+=num*0.1
if  num % 2 == 0:
    scores += 1
elif num % 10 == 5:
    scores+=2
print(scores)
print(num+scores)