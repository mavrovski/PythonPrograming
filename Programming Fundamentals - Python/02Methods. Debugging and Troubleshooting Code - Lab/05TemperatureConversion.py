def fahrenheit_to_celsius(fahrenheit):
    return float(fahrenheit-32)*5/9

n = float(input())
fahrenheitTemperature = fahrenheit_to_celsius(n)
print("%.2f" %fahrenheitTemperature)