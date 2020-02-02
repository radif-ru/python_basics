"""Задание 5.

Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""
from functools import reduce

user_list = [n for n in range(100, 1001) if not n % 2]
print(user_list)
user_list_multiplication = reduce(lambda x, y: x * y, user_list)
print(user_list_multiplication)
