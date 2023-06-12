# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных 
# чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя
# использовать циклы.
# *Пример:*
# 2 2
#     4 

def sumOfNumbers(A, B):
    if B == 0:
        return A
    else:
        return sumOfNumbers(A, B-1) + 1
    
numA = int(input("Введите число A: "))
numB = int(input("Введите число В: "))
print(f"А = {numA}, B = {numB} -> {sumOfNumbers(numA, numB)}")