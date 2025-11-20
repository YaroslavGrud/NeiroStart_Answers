import random
random.seed(42)
humidity = random.randint(1, 150)
# Переменная хранит в себе какое‑то число

if 30 <= humidity <= 50:
    print("Влажность комфортна")
else:
    print("Недостаточный уровень влажности")