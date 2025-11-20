import random
random.seed(44)
temperature = random.randint(1, 32)

if temperature <= 0:
    print("Очень холодно")
elif temperature <= 10:
    print("Холодно")
elif temperature <= 20:
    print("Прохладно")
elif temperature <= 30:
    print("Тепло")
else:
    print("Жарко")