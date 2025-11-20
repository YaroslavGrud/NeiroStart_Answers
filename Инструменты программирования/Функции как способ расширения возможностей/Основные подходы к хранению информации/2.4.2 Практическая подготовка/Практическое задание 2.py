# Инициализируем переменные для хранения результата
max_length = 0
longest_name = ''

# Открываем файл и читаем его содержимое
with open('names.txt', 'r', encoding='utf-8') as file:
    # Перебираем каждую строку в файле
    for line in file:
        # Удаляем пробелы и переносы строк
        name = line.strip()

        # Проверяем длину текущего имени
        if len(name) > max_length:
            max_length = len(name)  # обновляем максимальную длину
            longest_name = name  # сохраняем текущее имя

# Выводим результат
print(f"Самое длинное имя: {longest_name}")
