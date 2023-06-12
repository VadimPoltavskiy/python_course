# Напишите программу, которая на 
# вход принимает два числа A и B,
# и возводит число А в целую степень 
# B с помощью рекурсии.
#  *Пример:*
#  A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponentiation(A, B):
    if B == 0:
        return 1
    if B > 0:
        if B == 1:
          return A
        else:
            return exponentiation(A, B-1) * A
    else:
        if B == -1:
            return 1/A
        else:
            return exponentiation(A, B+1) / A
    
numA = int(input("Введите число A: "))
numB = int(input("Введите число В: "))
print(f"А = {numA}, B = {numB} -> {exponentiation(numA, numB)}")