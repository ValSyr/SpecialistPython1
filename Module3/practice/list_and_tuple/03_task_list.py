# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random
numbers = []
n = int(input("n: "))
i = 0
while i < n:
    number = random.randint(-10, 10)
    numbers.append(number)
    i += 1

s = 0
for el in numbers:
        s += el

print(s)
