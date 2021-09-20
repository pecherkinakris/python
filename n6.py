from itertools import count, cycle

start = int(input('Введите начало отсчета: '))
end = int(input('Введите конец отсчета: '))

for el in count(start) :
    if el > end :
        break
    else :
        print(el)


my_list = [a for a in range(1, 8)]
с = 0
for i in cycle(my_list):
    if с > 10:
        break
    print(i)
    с += 1
