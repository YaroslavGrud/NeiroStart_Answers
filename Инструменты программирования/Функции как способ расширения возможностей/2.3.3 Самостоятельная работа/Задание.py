def combine_and_unique(list1, list2):
    """
    Объединяет два списка и возвращает новый список с уникальными элементами.

    Параметры:
    list1 (list) — первый список
    list2 (list) — второй список

    Возвращает:
    list — новый список с уникальными элементами из обоих списков
    """
    unique_elements = []  # Создаём пустой список для уникальных элементов

    # Перебираем первый список
    for item in list1:
        if item not in unique_elements:  # Проверяем, что элемент ещё не добавлен
            unique_elements.append(item)  # Добавляем уникальный элемент

    # Перебираем второй список
    for item in list2:
        if item not in unique_elements:  # Проверяем, что элемент ещё не добавлен
            unique_elements.append(item)  # Добавляем уникальный элемент

    return unique_elements  # Возвращаем список с уникальными элементами


# Пример использования функции
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = combine_and_unique(list_a, list_b)
print(result)  # Вывод: [1, 2, 3, 4, 5, 6, 7, 8]