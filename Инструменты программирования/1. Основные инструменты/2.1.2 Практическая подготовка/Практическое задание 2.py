# Получаем входную строку
input_string = input()

# Разделяем строку на список слов
words_list = input_string.split()  # по умолчанию split() разделяет по пробелам

# Переворачиваем список слов
reversed_list = words_list[::-1]

# Собираем слова обратно в строку с пробелами
result = ' '.join(reversed_list)

# Выводим результат
print(result)