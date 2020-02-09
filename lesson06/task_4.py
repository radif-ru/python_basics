"""Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        return f'{self.color} {self.name} поехала'

    def stop(self):
        return f'{self.color} {self.name} остановилась'

    def turn(self, direction):
        return f'{self.color} {self.name} повернула на {direction}'

    def show_speed(self):
        if self.is_police:
            return f'Полицейская {self.color} {self.name} - {self.speed} км/ч'
        else:
            return f'{self.color} {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False, allowed_speed=60):
        super().__init__(speed, color, name, is_police)
        self.allowed_speed = allowed_speed

    def show_speed(self):
        if self.speed > self.allowed_speed:
            return f'{self.color} {self.name} превысила скорость на {self.speed - self.allowed_speed} км/ч'
        else:
            return f'{self.color} {self.name} - {self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False, allowed_speed=40):
        super().__init__(speed, color, name, is_police)
        self.allowed_speed = allowed_speed

    def show_speed(self):
        if self.speed > self.allowed_speed:
            return f'{self.color} {self.name} превысила скорость на {self.speed - self.allowed_speed} км/ч'
        else:
            return f'{self.color} {self.name} - {self.speed} км/ч'


class PoliceCar(Car):
    is_police = True


town_car = TownCar(180, 'green', 'Toyota Corolla')
print(town_car.turn('налево'), town_car.show_speed(), sep='\n')
sport_car = SportCar(240, 'red', 'Ferrari')
print(sport_car.go(), sport_car.show_speed(), sep='\n')
work_car = WorkCar(0, 'gray', 'Toyota Camry')
print(work_car.stop(), work_car.show_speed(), sep='\n')
police_car = PoliceCar(0, 'white', 'Ford Focus', True)
print(police_car.stop(), police_car.show_speed(), sep='\n')
