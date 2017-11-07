amount = float(input())
currencyFrom = input()
currencyTo = input()


def switch(amount,currencyFrom,currencyTo):
    result = 0.0
    toLeva = 0.0

    if currencyFrom == "BGN":
        toLeva = amount
    if currencyFrom == "USD":
        toLeva = amount * 1.79549
    if currencyFrom == "EUR":
        toLeva = amount * 1.95583
    if currencyFrom == "GBP":
        toLeva = amount * 2.53405

    if currencyTo == "BGN":
        result = toLeva
    if currencyTo == "USD":
        result = toLeva / 1.79549
    if currencyTo == "EUR":
        result = toLeva /1.95583
    if currencyTo == "GBP":
        result = toLeva / 2.53405
    return  result
    # print("{0:.2f} ".format(result)+currencyTo)
result = switch(amount,currencyFrom,currencyTo)
print("{0:.2f} ".format(result)+currencyTo)