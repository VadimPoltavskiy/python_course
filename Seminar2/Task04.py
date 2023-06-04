from random import randint
days = int(input("Введите колличсество дней: "))
temp = 1
count = 0
totalDays = 0
for i in range(days):
    temp += randint (-3, 3)
    print (temp)

    if temp > 0:
        count += 1
    else:
        if totalDays < count:
            totalDays = count
        count = 0
print (totalDays)

