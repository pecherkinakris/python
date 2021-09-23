f = open("myfileN2.txt")

line = f.readlines()
print(f'Колличество строк в документе - {len(line)}')


with open("myfileN2.txt") as f:
    i = 0
    for line in f.readlines():
        words = len(line.split(' '))
        i += 1
        print(f'В {i} строке {words} словa')
