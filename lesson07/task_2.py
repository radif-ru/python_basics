"""Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(Clothes):
    def __init__(self, the_size, name='default'):
        super().__init__(name)
        self.name, self.the_size = name, the_size

    @property
    def tissue_consumption(self):
        return self.the_size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height, name='default'):
        super().__init__(name)
        self.name, self.height = name, height

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3


coat = Coat(23)
print(f'Расход ткани на пальто: {coat.tissue_consumption:.2f}')

costume = Costume(23, name='super-puper')
print(f'Расход ткани на костюм: {costume.tissue_consumption:.2f}')

print(f'Общий расход ткани: {coat + costume:.2f}')
