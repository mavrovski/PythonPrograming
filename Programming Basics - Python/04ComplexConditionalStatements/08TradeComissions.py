city = input().lower()
sales = float(input())
result = 0.0
commission = 0.0
if city !="sofia" and city !="varna" and city !="plovdiv":
    print("error")
else:
    if city == "sofia":
        if sales >=0 and sales <=500:
            commission = 0.05
        elif sales >500 and sales <=1000:
            commission = 0.07
        elif sales > 1000 and sales <= 10000:
            commission = 0.08
        elif sales > 10000:
            commission = 0.12
    elif city == "varna":
        if sales >=0 and sales <=500:
            commission = 0.045
        elif sales >500 and sales <=1000:
            commission = 0.075
        elif sales > 1000 and sales <= 10000:
            commission = 0.10
        elif sales > 10000:
            commission = 0.13
    elif city == "plovdiv":
        if sales >=0 and sales <=500:
            commission = 0.055
        elif sales >500 and sales <=1000:
            commission = 0.08
        elif sales > 1000 and sales <= 10000:
            commission = 0.12
        elif sales > 10000:
            commission = 0.145

    result = sales*commission

    if result>0.0:
        print("{0:.2f}".format(result))
    else:
        print("error")

