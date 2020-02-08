"""Задание 5.

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
with open('numbers.txt', 'w+', encoding='utf-8') as f:
    while True:
        num = input('Введите число: ')
        if not num:
            break
        f.write(f'{num} ')
    if f.tell() > 0:
        f.seek(0)
        nums = f.read().rstrip().split(' ')
        sum_nums = sum(map(float, nums))
        print(f'{sum_nums:.2f}')
