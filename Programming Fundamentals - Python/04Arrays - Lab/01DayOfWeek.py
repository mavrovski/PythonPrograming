n = int(input())
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
if n>=1 and n<=7:
    print(days[n - 1])
else:
    print("Invalid Day!")