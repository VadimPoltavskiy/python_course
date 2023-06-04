
# Задача на смещение элеменов списка на несколько мест

from random import randint
lis = list()
lens = int(input("Введите длину списка: "))
for i in range(lens):
    lis.append(randint(0,10))
print(lis)
k = int(input("введите длину отступа: "))
for i in range(k):
    lis.insert (0, lis.pop(len(lis)-1))
print(lis)