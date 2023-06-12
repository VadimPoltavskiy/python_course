# Даны два массива чисел. Требуется вывести  те элементы первого массива
# (в том порядке), в котором они идут в первом массиве), которых нет во втором массиве
from random import randint
my_list = [randint(0,10) for i in range(15)]
my_list1 = [randint(0,10) for i in range(5)]
new_list = []
for i in my_list:
    if i not in my_list1:
        new_list.append(i)
print(new_list)