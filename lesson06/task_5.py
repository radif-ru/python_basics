"""Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:
    def __init__(self, title='Стандарт'):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки. Название: {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой. Название: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом. Название: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером. Название: {self.title}'


stationery, pen, pencil, handle = Stationery(), Pen('Erich Krause'), Pencil('Super-Puper'), Handle('Fat')
print(stationery.draw(), pen.draw(), pencil.draw(), handle.draw(), sep='\n')
