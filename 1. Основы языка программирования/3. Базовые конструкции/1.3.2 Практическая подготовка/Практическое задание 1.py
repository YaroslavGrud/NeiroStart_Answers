import random
random.seed(61)
x = random.randint(14, 25)

if 10 <= x <= 20:
    x = x + 5
else:
    x = x - 3

print(x)