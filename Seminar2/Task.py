# Дано натурально число А > 1.
# определите, какие по счету числом Фибоначи оно является,
# то есть выводите такое число n, что ф(n) = А.
# Если А не является число Фибоначчи, выведите число -1.
number = int (input("Введите число: "))
i = 3
fibOne = 0
fibTwo = 1
answer =  fibOne + fibTwo
while answer < number:
    fibOne = fibTwo
    fibTwo = answer
    answer = fibOne + fibTwo
    i += 1
if number == answer:
    print(i)
else:
    print(-1)