"""Задания 4,5,6.

4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt + '\nВыполнение кода прекращено!')
        exit()


class Warehouse:
    def __init__(self):
        self._equipments = {}

    def __add__(self, other):
        self.add_equipments(other)

    def __str__(self):
        return self.get_equipments

    def __getitem__(self, key):
        return self.get_equipment(key)

    def add_equipments(self, *args):
        for el in args:
            key_dict = el.__class__.__name__
            if self._equipments.get(key_dict):
                self._equipments[key_dict].append(el)
            else:
                self._equipments.update({key_dict: [el]})

    @property
    def get_equipments(self):
        equipments_dict = {}
        for key, val in self._equipments.items():
            equipments_dict.update({key: []})
            for el in val:
                equipments_dict[key].append(el.__dict__)
        return equipments_dict

    def get_equipment(self, key):
        equipment_list = []
        for i, el in enumerate(self._equipments[key], 0):
            equipment_list.append(self._equipments[key][i].__dict__)
        return equipment_list


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = self.is_digit(price)

    @staticmethod
    def is_digit(string):
        if str(string).isdigit():
            return string
        else:
            try:
                float(string)
                return string
            except ValueError as e:
                print(e)
                raise OwnError('Необходимо ввести число!')


class Printer(OfficeEquipment):
    def __init__(self, name, price, is_color):
        super().__init__(name, price)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, name, price, dpi):
        super().__init__(name, price)
        self.dpi = dpi


class Xerox(OfficeEquipment):
    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed


printer = Printer('Canon', 2150, True)
scanner = Scanner('Vmn', 1000, 800)
xerox = Xerox('HUGO', 2000, 56)
print(printer.name, printer.price, 'Color' if printer.is_color else 'BlackAndWhite')

warehouse = Warehouse()
warehouse.add_equipments(printer, xerox, scanner)
warehouse + Xerox('qwerty', 2000, 56)
warehouse + Scanner('raizer', 103400, 8500)

print(warehouse.get_equipments)
print(warehouse['Printer'])

printer = Printer('Canon', 'qwe', True)
