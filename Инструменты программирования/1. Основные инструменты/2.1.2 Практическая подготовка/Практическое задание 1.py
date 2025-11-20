# Получаем текст от пользователя
text = input()

# Преобразуем текст к нижнему регистру
text_lower = text.lower()

# Подготавливаем список возможных вариантов имени с учётом знаков препинания.
# Используем метод split для разбивки текста на слова
words = text_lower.split()

# Очищаем каждое слово от знаков препинания в начале и конце
import string
cleaned_words = [word.strip(string.punctuation) for word in words]

# Подсчитываем точное количество вхождений слова "Иван"
count = cleaned_words.count("иван")

# Выводим результат
print(count)
