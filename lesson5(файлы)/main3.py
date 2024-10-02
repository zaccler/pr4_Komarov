import csv

a = input("Введите имя файла: ")
b = int(input("Введите число: "))

try:
    with open(f"..\\python\\lesson5(файлы)\\files\\{a}", 'r', encoding='utf-8') as f:
        buff = []
        i = 1
        for line in f:
            if line.strip():  # если строка не пустая
                buff.append(line)
            if len(buff) == b:  # если достигнуто заданное количество строк (b)
                with open(f'..\\python\\lesson5(файлы)\\files\\output\\{i}.txt', 'w', encoding='utf-8') as output:
                    output.write(''.join(buff))
                i += 1
                buff = []
        # Если есть остаток строк в буфере, записать его в новый файл
        if buff:
            with open(f'..\\python\\lesson5(файлы)\\files\\output\\{i}.txt', 'w', encoding='utf-8') as output:
                output.write(''.join(buff))
except OSError:
    print("Ошибка, файла не существует((")
    exit()