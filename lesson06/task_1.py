"""Задание 1.

Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.

"""
from itertools import cycle
from time import sleep


class TrafficLight:
    ___color = [['red', 'yellow', 'green'], ['красный', 'желтый', 'зеленый'], [1, 2, 3]]

    def running(self, use_colors=None):
        if use_colors and use_colors not in self.___color:
            print('Нарушение порядка режимов!')
        else:
            use_colors = self.___color[0] if not use_colors else use_colors
            zip_colors = list(zip(*self.___color))
            for color in cycle(use_colors):
                print(color)
                if color in zip_colors[0]:
                    sleep(7)
                elif color in zip_colors[1]:
                    sleep(2)
                elif color in zip_colors[2]:
                    sleep(1)


traffic_light = TrafficLight()
# Порядок режимов нарушен:
traffic_light.running(['red', 'green', 'yellow'])
traffic_light.running(['зеленый', 'желтый', 'красный'])
# Порядок режимов верный(возможен вызов метода без передачи параметров, тогда будет отображаться
# английский список по умолчанию):
traffic_light.running(['красный', 'желтый', 'зеленый'])
