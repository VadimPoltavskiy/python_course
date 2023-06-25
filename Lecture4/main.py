def f(x):
    return x ** 2
print(f(2))

def f(x):
    return x ** 2
g = f

def f(x):
    return x ** 2
g = f
print(f(4)) # 16
print(g(4)) # 16

def calc1(x):
    return x + 10
print(calc1(10)) # 20

def calc2(x):
    return x * 10
def math(op, x):
    print(op, x)
math(calc2, 10) # 100

def sum(x, y):
    return x + y
def mylt(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
calc(mylt, 4, 5) # 20

def sum(x, y):
    return x + y
f = sum
calc(f, 4, 5) # 9

def sum(x, y):
    return x + y # ⇔ (равносильно) sum = lambda x, y: x + y

calc(lambda x, y: x + y, 4, 5) # 9

data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out)

def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))

list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)

data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

data = list(map(int,input().split()))

def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]

lambda x: x % 2 == 0

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14),
('user5', 7)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

with open('file.txt', 'w') as data:
data.write('line 1\n')
data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
print(line)
data.close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()

import os
os.chdir('C:/Users/79190/PycharmProjects/GB')

import os
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'


import os
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #
'main.py'

import os
print(os.path.abspath('main.py'))
# 'C:/Users/79190/PycharmProjects/webproject/main.py'



