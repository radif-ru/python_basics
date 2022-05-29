"""Задание 7.

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, num_1, num_2=0):
        self.num_1, self.num_2 = num_1, num_2

    def __add__(self, other):
        return complex(self.num_1, self.num_2) + complex(other.num_1, other.num_2)

    def __mul__(self, other):
        return complex(self.num_1, self.num_2) * complex(other.num_1, other.num_2)


complex_1 = ComplexNumber(22, 2)
complex_2 = ComplexNumber(23, 2)

print(complex_1 + complex_2)
print(complex_1 * complex_2)
