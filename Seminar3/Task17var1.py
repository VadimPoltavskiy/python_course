#Дан список чисел. определите, сколько в нем встречается различных списков
import random
from random import randint
myList = []
for i in range(10):
    myList.append(random.randint(0,10))
print (myList)
myList = set(myList) #Переводим во множесто значений 
print (myList)
print(len(myList))