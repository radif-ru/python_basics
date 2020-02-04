"""Задание 1.

Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv

try:
    production_in_hours, rate_per_hour, *the_prize = [el for el in argv if el != argv[0]]
except ValueError as e:
    print(f'Недостаточно данных. Введите выработку в часах, ставку в час и премию(если есть). \nОшибка: {e}')
else:
    try:
        wage = float(production_in_hours) * float(rate_per_hour) + sum([float(el) for el in the_prize])
    except ValueError as e:
        print(f'Необходимо вводить только числа. \nОшибка: {e}')
    else:
        print(f'Зарплата составила: {wage:.2f}')
