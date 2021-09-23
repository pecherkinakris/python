rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_f = []

with open('myfileN4.txt') as f:
    for i in f:
        i = i.split(' ', 1)
        new_f.append(rus[i[0]] + ' ' + i[1])
    print(new_f)

with open('new_myfileN4.txt', 'w') as f_2:
    f_2.writelines(new_f)
