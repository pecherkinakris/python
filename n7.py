from math import factorial

def func():
    for el in range(1, n + 1):
        yield factorial(el)

n = int(input('Введите n: '))

fact = func()
x = 0
for i in fact:
    if x < n:
        print(i)
        x += 1
    else:
        break