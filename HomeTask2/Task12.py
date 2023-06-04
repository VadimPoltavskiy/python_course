# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math
sum = int (input("Введите сумму чисел: "))
multiplication = int (input("Введите произведение чисел: "))
# number2*number2 - sum * number2 + multiplication = 0
a = 1
b = -sum
c = multiplication
discr = b ** 2 - 4 * a * c
if discr > 0:
    number1 = (-b + math.sqrt(discr)) // (2 * a)
    number2 = (-b - math.sqrt(discr)) // (2 * a)
elif discr == 0:
    number2 = -b // (2 * a)
    number1 = number2

if (number1 + number2 == sum and number1 * number2 == multiplication):
    print(f"первое число = {number2}, второе число = {number2}")
else:
    print(f"не существует таких значений при которых сумма = {sum}, а произведение = {multiplication}")
