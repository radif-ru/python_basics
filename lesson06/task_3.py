"""Задание 3.

Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}, должность - {self.position}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_position = Position('Петров', 'Инокентий', 'фрезеровщик', 55000, 150)
print(worker_position.name, worker_position.surname, worker_position.position, worker_position._income, end='\n\n')
print(worker_position.get_full_name())
print(worker_position.get_total_income())
