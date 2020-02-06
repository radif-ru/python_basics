j = 2
i = 3
print(complex(5, 6))

bla = 'safasfasfsdr3253634vzvdz'
print(list(bla[1:10:3]))
print(list(bla)[1:10:3])
lis = list(bla)
lis.append(00000)
lis = str(lis)

a = (1, 2, 'qwe', 23)
b = (1, 2, 'qwe', 23)

print(id(a))
print(id(b), a is b)

set_dict = {1, 2, 4, 'ad'}
set_dict.discard('ad')
print(set_dict)

hum = {'asaf': 1241, 24: 'asfsaf', 'qwe': 'asd', 'SADAS': 244, 243: 324, 'AFAS': 'ASDA'}
print(24 in hum.keys(), hum.keys())
print(hum.popitem(), hum.pop(24))

dfg = [1, 2, 'asf']
dfg.pop()

print(hum.items())
for k, v in hum.items():
    print(k, v)

for k in hum:
    print(k)

for k in hum.keys():
    print(k)

for k in hum.values():
    print(k)

print(int(17.5))
print(int('10001', 2))
print(bin(17))
print(oct(17))
print(hex(193295299327))

n_2 = complex(7, 8)
print(n_2)

s = 'abrakadabra'
print(s[4:7])
print(s[3:-3])
print(s[:5])
print(s[3:])
print(s[:])
print(s[::-1])
print(s[1:7:2])


def my_str_reverse(string):
    return string[::-1]


print(my_str_reverse("abrakadbra"))

for el in reversed("abrakadbra"):
    print(el)


def my_str_reverse(string):
    symbols = list(string)
    for el in range(len(string) // 2):
        tmp = symbols[el]
        symbols[el] = symbols[len(string) - el - 1]
        symbols[len(string) - el - 1] = tmp
        print(el, tmp, symbols[el], symbols[len(string) - el - 1])
    return ''.join(symbols)


data = my_str_reverse("abrakadabra12")
print(data)

print("one two free"[::-1].split())

print('_'.join(['раз', 'два', 'три']))
print(''.join(['раз', 'два', 'три']))
print("ехал грека через реку".title())
print('простая строка'.upper())

print(chr(33))

result_list = [2, 'text', 456, 45.3, None]
result_list.extend([8, 9, 10])
print(result_list)

result_list = [2, 'text', 456, 45.3, None, True]
result_list.insert(1, "ins_el")
print(result_list)

result_list.insert(result_list.index(result_list[-1::][0]), "ins_el")
print(result_list)

my_list = [10, 20, 30]
print((40 or 50 or 10) in my_list)

my_l = [4, 234, 45.8, "text", "word", "el", True, None]
print(my_l.__sizeof__())

my_t = (4, 234, 45.8, "text", "word", "el", True, None)
print(my_t.__sizeof__())

print(my_t.index(None))

perem_1 = {'b', 'd', 'r', 'a', 'k'}
perem_2 = frozenset('abrakadabra')
print(perem_1)
print(perem_2)
perem_1.add('!')
print(perem_1)
# perem_2.add('!')
# print(perem_2)
perem_1.pop()
print(perem_1)

print(frozenset({'r', 'a', 'd', 'k', 'b'}) is frozenset({'d', 'b', 'k', 'a', 'r'}))

my_dict = dict(key_1='val_1', key_2='val_2')
print(my_dict)
my_dict.popitem()

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}
print(my_dict.keys())

my_dict = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 40, 'position': None}
for el in my_dict:
    if my_dict[el] == None:
        print(f"Для сотрудника пока не определен параметр: {el}")

for i in 'sdad':
    print(i)

checked = True
personality = ("проверено", "не проверено")[checked]
print(personality)

print(True or "Some")
print(False or "Some")

func_return = None
message = func_return or "Функция ничего не возвращает"
print(message)

var_1, var_2, var_3 = [20, 30, 'asdas']
print(var_1, var_2, var_3)
var_1, var_2, var_3 = var_3, var_2, var_1
print(var_1, var_2, var_3)

var_1, var_2, var_3 = range(3)
print(var_1, var_2, var_3)
var_1, var_2, var_3 = var_3, var_2, var_1
print(var_1, var_2, var_3)

my_list = [10, 20, 20, 20, 30, 50, 70, 30]
print(max(my_list))

my_list = [20, 30, 40, 50]
*el_1, el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, *el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, *el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, el_3, *el_4 = my_list
print(el_1, el_2, el_3, el_4)
el_1, el_2, el_3, el_4, *el_5 = my_list
print(el_1, el_2, el_3, el_4, el_5)

my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict))

my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict, key=my_dict.get))

for ind, el in enumerate(['ноль', 'один', 'два', 'три']):
    print(ind, el)

for ind, el in enumerate(['один', 'два', 'три'], 1):
    print(ind, el)

print(list(enumerate(['ноль', 'один', 'два', 'три'])))

old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)
print(list(new_list))


def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2

    return int_func


f_obj = ext_func(200)  # f_obj - функция
print(id(0x038ED898))
print(f_obj(300))


def s_calc():
    try:
        # r_val = float(input("Укажите радиус: "))
        # h_val = float(input("Укажите высоту: "))
        r_val = 2141
        h_val = 2424
    except ValueError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_side, s_full


s_side_val, s_full_val = s_calc()
print(f"Площадь боковой пов-ти - {s_side_val}; Полная площадь - {s_full_val}")
sd = s_calc()
print(type(sd), sd, s_calc())

my_func = lambda p_1, p_2: p_1 + p_2

print(my_func(2, 5))
print(my_func("abra", "kadabra"))

print((lambda p_1, p_2: p_1 + p_2)(2, 5))
print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))

new_func = lambda *args: args
print(new_func(10, 20, 30, 40))
p_1 = 24141
p_2 = 32532532
print((lambda p_1, p_2: p_1 + p_2)(p_1, p_2))


def named_func(param):
    return param ** 0.5


print(named_func(100))

square_rt = lambda param: param ** 0.5
print(square_rt(100))

print(ord('ё'), chr(335))

print(divmod(25, 2), 25 // 2, 25 % 2)

print(pow(2, 4), 2 ** 4)

print(list(range(1, -7, -2)))


def full_s_calc():
    global r_val, h_val, s_side, s_circle
    r_val = 2342
    h_val = 324
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full


s_val = full_s_calc()
print(full_s_calc())
print(s_circle)
s_circle = 1
print(s_circle)


def ext_func():
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var

    return int_func


func_obj = ext_func()
print(func_obj)
print(func_obj())
print(func_obj())
print(func_obj())
print(bytes(90))

print(callable(ext_func()))

print(dir())

print('1.1'.isdigit())

# import time
# import random
# print(time.time())
# print(random.random())
#
# from sys import argv
#
# script_name, first_param, *second_param, third_param = argv
#
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)
# print("Параметр 2: ", second_param)
# print("Параметр 3: ", third_param)

# lines = [line.lstrip().rstrip()for line in open('text.txt')]
# print(lines)

str_1 = "abc"
str_2 = "d"
str_3 = "efg"
sets = [i + j + k for i in str_1 for j in str_2 for k in str_3]
print(sets)

# В этом примере результат выполнения функции random() умножается на 6.
# В результате получаем число от 0 до 6. Прибавляем 4 и получаем число от 4 до 10.
from random import *

print(random() * (10 - 4) + 4)

print(uniform(12213.213123123, 241224.24141241242142))
print(randint(12213, 241224))

generator = (param * param for param in range(5))

print(next(generator))
print(next(generator))
print(next(generator))
[print(el) for el in generator]


def generator():
    for el in (10, 20, 30):
        yield el
    yield 2 ** 6


g = generator()
print(g)

for el in g:
    print(el)

from functools import *


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


print(reduce(my_func, [10, 20, 30]))


def my_func(param_1, param_2, asad):
    return param_1 ** param_2 * asad


new_my_func = partial(my_func, 2, 2)
print(new_my_func)
print(new_my_func(4))
print(new_my_func(3))

from itertools import *
import time

t1 = time.time()
time.sleep(0.00001)
for el in count(7):
    if el > 15:
        break
    else:
        print(el)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
time.sleep(0.00001)
for el in range(7, 700000000000000000000000000000):
    if el > 15:
        break
    else:
        print(el)
t2 = time.time()
print(t2 - t1)

c = 0
for el in cycle("ABC"):
    if c > 10:
        break
    print(el)
    c += 1

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

from math import ceil, fabs, factorial, floor, \
    fmod, isfinite, modf, sqrt, sin, cos, tan, degrees, radians

print(f"ceil() -> {ceil(6.75)}")
print(f"fabs() -> {fabs(-4)}")
print(f"factorial() -> {factorial(5)}")
print(f"floor() -> {floor(4.34)}")
print(f"fmod() -> {fmod(9, 4)}")
print(f"isfinite() -> {isfinite(10)}")
print(f"modf() -> {modf(10.5)}")
print(f"sqrt() -> {sqrt(16)}")
print(f"sin() -> {sin(1.5708)}")
print(f"cos() -> {cos(1.5708)}")
print(f"tan() -> {tan(1.5708)}")
print(f"degrees() -> {degrees(1.5708)}")
print(f"radians() -> {radians(90)}")

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([num1 for num1, num2 in zip(source_list[1:], source_list[:-1]) if num1 > num2])
print([num for i, num in enumerate(source_list) if i > 0 and num > source_list[i-1]])
