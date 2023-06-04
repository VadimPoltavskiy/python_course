# Вычесление факториала

n = int(input("Введите число n: "))
i = 1
faktorial = 1
while i <= n:
    faktorial = faktorial * i
    i += 1
print(faktorial)