"""Задание 2.

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""
with open('file.txt', 'r', encoding='utf-8') as f:
    lines = [line.rstrip() for line in f.readlines()]
    f.seek(0)
    words = f.read().split(' ')
    print(f'Количество строк: {len(lines)}')
    for num, line in enumerate(lines, 1):
        print(f'Количество слов в {num} строке: {len(line.split())}')
