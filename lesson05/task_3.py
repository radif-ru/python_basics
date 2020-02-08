"""Задание 3.

Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
with open('employee_salaries.txt', 'r', encoding='utf-8') as f:
    lines_list = [line.rstrip() for line in f.readlines()]
    print(lines_list)
    salaries_sum = 0
    for line in lines_list:
        line_list = line.split()
        if float(line_list[1]) < 20000:
            print(f'У {line_list[0]} зарплата менее 20 тыс.')
        salaries_sum += float(line_list[1])
    average_salary = salaries_sum / len(line_list)
    print(average_salary)
