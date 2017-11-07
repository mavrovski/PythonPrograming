product = input().lower()
dayOfWeek = input().lower()
quantity = float(input())
# days = ['monday',  'tuesday',  'wednesday',  'thursday', 'friday', 'saturday', 'sunday']

banana = 0.0
apple =0.0
orange =0.0
grapefruit = 0.0
kiwi = 0.0
pineapple = 0.0
grapes = 0.0
if dayOfWeek !="monday" and dayOfWeek != 'tuesday' and \
                dayOfWeek != 'wednesday' and dayOfWeek != 'thursday' and \
                dayOfWeek != 'friday' and dayOfWeek != 'saturday' and dayOfWeek != 'sunday':
  print("Error")
else:
    if dayOfWeek == "saturday" or dayOfWeek == 'sunday':
        if product == "banana":
            banana = 2.70
            print("{0:.2f}".format(banana * quantity))
        elif product == "apple":
            apple = 1.25
            print("{0:.2f}".format(apple * quantity))
        elif product == "orange":
            orange = 0.90
            print("{0:.2f}".format(orange * quantity))
        elif product == "grapefruit":
            grapefruit = 1.60
            print("{0:.2f}".format(grapefruit * quantity))
        elif product == "kiwi":
            kiwi = 3.00
            print("{0:.2f}".format(kiwi * quantity))
        elif product == "pineapple":
            pineapple = 5.60
            print("{0:.2f}".format(pineapple * quantity))
        elif product == "grapes":
            grapes = 4.20
            print("{0:.2f}".format(grapes * quantity))
        else:
            print("Error")

    else:
        if product == "banana":
            banana = 2.50
            print("{0:.2f}".format(banana * quantity))
        elif product == "apple":
            apple = 1.20
            print("{0:.2f}".format(apple * quantity))
        elif product == "orange":
            orange = 0.85
            print("{0:.2f}".format(orange * quantity))
        elif product == "grapefruit":
            grapefruit = 1.45
            print("{0:.2f}".format(grapefruit * quantity))
        elif product == "kiwi":
            kiwi = 2.70
            print("{0:.2f}".format(kiwi * quantity))
        elif product == "pineapple":
            pineapple = 5.50
            print("{0:.2f}".format(pineapple * quantity))
        elif product == "grapes":
            grapes = 3.85
            print(round((grapes * quantity), 3))
        else:
            print("Error")




