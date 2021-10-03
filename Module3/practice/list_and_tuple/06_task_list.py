# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.



first_number = int(input("1n= "))  # Первое число
second_number = int(input("2n ="))  # Второе число

numbers = [first_number, second_number]

for new_number in numbers:
    if new_number % 3==0:
        print(new_number)
