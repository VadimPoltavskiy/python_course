# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
my_list = [randint(0,10) for i in range(6)]
print(my_list)
min_num = int(input("Введите минимальное значение: "))
max_num = int(input("Введите максимальное значение: "))
for i in range(len(my_list)):
    if min_num <= my_list[i] <= max_num:
        print(i)