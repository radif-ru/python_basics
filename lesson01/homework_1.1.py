"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

variable = 'Hello World'
print(f'Переменная: {variable}, тип: {type(variable)}')
variable = 12345
print(f'Переменная: {variable}, тип: {type(variable)}')
variable = 12345.13124
print(f'Переменная: {variable}, тип: {type(variable)}')

variable_string = input('Введите строку: ')
variable_int = float(input('Введите число: '))
print(f'Вы ввели число: {variable_int:.2f}, округлённое до сотых и строку: {variable_string}')