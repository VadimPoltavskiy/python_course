from random import randint
countWater = int(input("Введите колличество арбузов: "))
minWater = float("inf")  #Бесконечно большое число
maxWater = float("-inf") #Бесконечно маленькое число
for i in range (countWater):
    weight = randint (1, 50)
    if weight < minWater:
        minWater = weight
    if weight > maxWater:
        maxWater = weight
print (minWater, maxWater)