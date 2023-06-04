#Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

digit = int(input("Введите трехзначное число: "))
if (digit > 99 and digit < 1000 ):
    total = digit % 10
    numder = digit // 10
    total = total + numder % 10
    numder = numder // 10
    total = total + numder % 10
    print (f"{digit} --> {total}")
else:
    print ("Введено не трехзначное число")
