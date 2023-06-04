# дан список состоящий из целый чисел. напишите программу.
# которая подсчитает количество элементов списка,
# больших предыдущего (элемента с предыдущим номером)

import random
from random import randint
myList = []
lens = int(input("Введите длину массива: "))
for i in range(lens):
    myList.append(random.randint(0,10))
print (myList)
count = 0
for i in range (len(myList)-1):
    if myList[i+1] > myList[i]:
        count += 1
print (count)
