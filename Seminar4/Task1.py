# напишите программу, которая на вход принимает строку.
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к симолам с помошью постфикса формата _n.
import random
my_list = [random.randint(0,10) for _ in range(20)]
print(my_list)
counter= {}

for item in my_list:
    counter[item] = counter.get(item, 0) + 1
    if counter.get(item)< 2:
        print(item, end=" ")
    else:
        print(str(item) + "_"+ str(counter.get(item)- 1), end=" ")
    # print(item if counter.get(item)< 2 else (str(item) + "_"+ str(counter.get(item)- 1)), end=" ")
print(counter)