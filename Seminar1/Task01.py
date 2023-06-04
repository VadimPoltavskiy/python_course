# n = 700  
# m = 750
# x = m // n + (m % n > 0)
# print (x)

dist = int(input("Сколько машина проезжает за день: "))
total = int (input("Сколько надо проехать: "))

print (f"Машине понадобится {int((total + dist - 0.1) // dist)} дней")


import math

number = float (input("Введите число: "))


print (number)

print (round(number, 0))
print (math.ceil(number))
print (math.floor(number))