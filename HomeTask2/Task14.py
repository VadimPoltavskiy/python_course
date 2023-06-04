#Требуется вывести все целые степени двойки 
#(т.е. числа вида 2k), не превосходящие числа N.


digit = int(input("Введите число N: "))
count = 1
print (f"{digit} ->", end =" ")
while digit > count:
    print (f"{count}", end =" ")
    count *= 2
