import csv

count = 1
a = str(input("Введите имя файла: "))
n = int(input("Введите кол-во строк для вывода: "))
try:
    f = open(f"..\\python\\lesson5(файлы)\\files\\{a}",'r')
    
    for line in f:
        print(f'{count} ' + line.rstrip())
        count +=1
        if count - 1 == n:
            break
except OSError:
    print("Ошибка, файла не существует((")
    exit






