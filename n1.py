f = open("myfileN1.txt", "w")
text = input("Введите текст: \n")

while text:
    f.writelines(text + '\n')
    text = input('Введите текст: \n')
    if not text:
        break


f.close()
f = open('myfileN1.txt', 'r')
content = f.readlines()
print(content)
f.close()