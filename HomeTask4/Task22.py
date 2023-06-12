length1 = int(input("Введите количество элементов первого множества: "))
length2 = int(input("Введите количество элементов второго множества: "))

print(f"Введите элементы первого множества ({length1} значений): ")
list_1 = list() 
for i in range(length1): 
    n = int(input()) 
    list_1.append(n) 

print(f"Введите элементы второго множества ({length2} значений): ")
list_2 = list() 
for i in range(length2): 
    m = int(input()) 
    list_2.append(m) 

list_3 = list() 
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)
list_3.sort()
list_3 =list(set(list_3))
for k in list_3:
    print(k, end= " ")