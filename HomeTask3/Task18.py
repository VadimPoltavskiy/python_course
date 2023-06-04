# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#    *Пример:*
#    5
#    1 2 3 4 5
#    6
#    -> 5

import random
from random import randint
myList = []
len = int(input("Введите длину массива: "))
searchingNumber = int(input("Введите искомое число: "))
dif2 = float("inf")
for i in range(len):
    myList.append(random.randint(0,100))
    if myList[i] > searchingNumber:
        dif1 = myList[i] - searchingNumber
    else:
        dif1 = searchingNumber - myList[i]

    if dif1 < dif2:
        dif2 = dif1
        index = i
print (f"{myList} Искомое значение: {searchingNumber}  -> Ближайшее значение {myList[index]}")