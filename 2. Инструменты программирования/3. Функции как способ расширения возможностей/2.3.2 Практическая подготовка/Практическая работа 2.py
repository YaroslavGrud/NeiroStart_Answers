def convert_time(minutes):
    hours = minutes // 60  # Вычисляем количество полных часов
    remaining_minutes = minutes % 60  # Вычисляем оставшиеся минуты
    print(f"Время: {hours} ч {remaining_minutes} минут")

# Пример вызова функции
convert_time(145)
