from random import randint
my_list = [randint(0,10) for i in range(15)]
count = 0
for i in range(1, len(my_list)-1):
    if my_list[i-1] < my_list[i] > my_list[i+1]:
        count += 1
print (my_list)
print (count)