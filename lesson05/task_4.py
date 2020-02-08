"""Задание 4.

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
}

with open('eng_nums.txt', 'r', encoding='utf-8') as f:
    rus_nums = []
    for line in f.readlines():
        new_line = line.split()
        new_line[0] = num_dict[new_line[0].lower()]
        rus_nums.append(f'{new_line[0].capitalize()} {new_line[1]} {new_line[2]}\n')
    with open('rus_nums.txt', 'w', encoding='utf-8') as f2:
        f2.writelines(rus_nums)
