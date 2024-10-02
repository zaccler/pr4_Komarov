import os.path

a = str(input("Введите имя файла: "))
b = str(input("Введите строку: "))
f = open(f"..\\python\\lesson5(файлы)\\files\\{a}",'w')
while b != '':
    f.write(f"{b}\n")
    b = str(input("Введите строку: "))
f.close()





