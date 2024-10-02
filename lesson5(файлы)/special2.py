a = str(input("Введите имя файла: "))
n = int(input("Введите кол-во строк для вывода: "))

try:
    with open(f"..\\python\\lesson5(файлы)\\files\\{a}", 'r', encoding='utf-8') as f:
        lines = f.readlines()  
        last_n_lines = lines[-n:]  # Получаем последние n строк списка
        
        count = 1
        for line in last_n_lines:
            print(f'{count} {line.strip()}')  # Выводим строки без лишних символов
            count += 1
except OSError:
    print("Ошибка, файла не существует((")
    exit()