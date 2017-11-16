def get(new_price,last_price,difference,ether_true_or_false):
    to = ""
    # ether_true_or_false = True
    if difference == 0:
        to = "NO CHANGE: {0:.2g}".format(new_price)

    elif  ether_true_or_false != True:
        to = "MINOR CHANGE: {0:.2g} to {1:.2g} ({2:.2f}%)".format(last_price,new_price,difference*100)

    elif ether_true_or_false and (difference>0):
        to = "PRICE UP: {0:.2g} to {1:.2g} ({2:.2f}%)".format(last_price,new_price,difference*100)

    elif ether_true_or_false and (difference<0):
        to = "PRICE DOWN: {0:.2g} to {1:.2g} ({2:.2f}%)".format(last_price,new_price,difference*100)

    return to

def is_difference(border,is_diff):
    if abs(border)>=is_diff:
        return True
    return False

def percent_calculation(old_price,new_price):
    percent = (new_price-old_price)/old_price
    return percent

number = int(input())
border = float(input())
last_price = float(input())

for i in range (0,number-1):
    new_price = float(input())
    div = percent_calculation(last_price,new_price)
    is_significant_difference = is_difference(div,border)
    message = get(new_price,last_price,div,is_significant_difference)
    print(message)
    last_price = new_price


