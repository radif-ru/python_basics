"""Задание 4.

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""


def exponentiation_function(x, y):
    return x ** y


def exponentiation_function2(x, y):
    result = x
    if not x:
        return '0 нельзя возвести в степень'
    for i in range(1, abs(y)):
        result *= x
    if y == 0:
        return 1
    elif y < 0:
        result = 1 / result
    return result


print(exponentiation_function(3.3, -3), exponentiation_function2(3.3, -3))
print(exponentiation_function(-3.3, -3), exponentiation_function2(-3.3, -3))
