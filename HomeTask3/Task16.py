# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое 
# число X в массиве A[1..N]. 
# Пользователь в первой строке вводит 
# натуральное число N – количество элементов
# в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит 
# число X
# *Пример:*
# 5
#    1 2 3 4 5
#    3
#    -> 1

import random
from random import randint
myList = []
len = int(input("Введите длину массива: "))
searchingNumber = int(input("Введите искомое число: "))
count = 0
for i in range(len):
    myList.append(random.randint(0,10))
    if myList[i] == searchingNumber:
        count += 1
print (f"{myList} Искомое значение: {searchingNumber}  -> {count}")

