n=int(input())

stars = 1
if n% 2 ==0:
    stars += 1
  # roof
for i in range(0,int((n+1)/2)):
    padding = int((n-stars)/2)
    print("-"*padding,end='')
    print("*" * stars, end='')
    print("-" * padding)
    stars +=2
    # body
for y in range(0,int(n/2)):
    print("|"+"*"*(n-2)+"|")