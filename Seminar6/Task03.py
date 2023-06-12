# дан список чисел. Подсичтайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.

from random import randint
my_list = [randint(0,5) for i in range(6)]
count = 0
for i in set(my_list):
    count += my_list.count(i) // 2
print (my_list)
print (count)