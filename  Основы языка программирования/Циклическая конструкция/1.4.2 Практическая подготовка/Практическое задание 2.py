numbers = [-10, 5, 3, -2, 9, 6, -1]
product = 1
# Начинаем с 1, так как это нейтральный элемент для умножения
for num in numbers:
    if num > 0:
        # Учитываем только положительные числа
        product *= num
print(product)
