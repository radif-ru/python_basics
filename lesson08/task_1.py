"""Задание 1.

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt + '\nВыполнение кода прекращено!')
        exit()


class Date:
    def __init__(self, date):
        self.date = date
        self.num_date(self.date)

    def __str__(self):
        return f'День: {self.day}, месяц: {self.month}, год: {self.year}'

    @classmethod
    def num_date(cls, num_date):
        cls.day, cls.month, cls.year = Date.val_date(list(map(int, num_date.split('-'))))

    @staticmethod
    def val_date(d_list):
        # весокосные года не учитываются
        if (d_list[0] > 31 and d_list[1] in [1, 3, 5, 7, 8, 10, 12]) or \
                (d_list[0] > 30 and d_list[1] in [4, 6, 9, 11]) or (d_list[0] > 29 and d_list[1] == 2):
            raise OwnError(f'Неверно указан день или месяц {d_list[0]}-{d_list[1]}')
        elif d_list[1] > 12:
            raise OwnError(f'Неверный месяц: {d_list[1]}')
        else:
            return d_list


my_date = Date('22-02-2020')
print(my_date)

Date.num_date('30-02-2020')
print(my_date)
