import random

tupe_list = [(random.randint(1, 4), random.randint(1, 4)) for _ in range(10)]
print(tupe_list)

tupe_list =list(filter(lambda x: x[0] != x[1], tupe_list))
print(tupe_list)

new_list =list(map(lambda x: 3.14 * x[0] * x[1], tupe_list))

for i in tupe_list:
    if i[0] * i[1] * 3.14  == max(new_list):
        print (i, max(new_list))
        break