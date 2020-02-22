""" Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f'{self.lists[0]:3} {self.lists[1]:3} {self.lists[2]:3}\n' \
               f'{self.lists[3]:3} {self.lists[4]:3} {self.lists[5]:3}'

    def __add__(self, next_matrix):
        self.lists = [sum(el) for el in zip(self.lists, next_matrix.lists)]
        return self.__str__()


matrix = Matrix([1, 2, 3, 4, 5, 6])
matrix2 = Matrix([5, 5, 5, 5, 5, 5])

print(matrix, matrix2, sep='\n' * 2, end='\n' * 3)

print(matrix + matrix2)


# Альтернативное решение:

# class Matrix:
#     def __init__(self, input_data):
#         self.input = input_data
#
#     def __str__(self):
#         return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.input])
#
#     def __add__(self, other):
#         answer = ''
#         if len(self.input) == len(other.input):
#             for line_1, line_2 in zip(self.input, other.input):
#                 if len(line_1) != len(line_2):
#                     return 'Problems with shape'
#
#                 summed_line = [x + y for x, y in zip(line_1, line_2)]
#                 answer += ' '.join([str(i) for i in summed_line]) + '\n'
#         else:
#             return 'Problems with shape'
#         return answer
#
#
#
# matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
# matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
#
# print(matrix_1)
# print()
# print(matrix_1 + matrix_2)
