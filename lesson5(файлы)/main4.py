def merge_files(file1, file2, output_file):
    try:
        with open(f"..\\python\\lesson5(файлы)\\files\\{file1}", 'r') as f1, open(f"..\\python\\lesson5(файлы)\\files\\{file2}", 'r') as f2, open(f"..\\python\\lesson5(файлы)\\files\\output\\output_file", 'w') as outfile:
            outfile.write(f1.read())
            outfile.write(f2.read())
        print(f"Файлы {file1} и {file2} успешно объединены в {output_file}.")
    except OSError as e:
        print(f"Ошибка при открытии файлов: {e}")

# Пример использования:
file1 = input("Введите имя файла: ")
file2 = input("Введите имя файла: ")
output_file = 'merged_file.txt'

merge_files(file1, file2, output_file)