import csv

count = 1
a = str(input("Введите имя файла: "))
try:
    f = open(f"..\\python\\lesson5(файлы)\\files\\{a}",'r')
    for line in f:
        print(f'{count} ' + line.rstrip())
        count +=1
except OSError:
    print("Ошибка, файла не существует((")
    exit






