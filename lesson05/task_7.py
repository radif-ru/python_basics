"""Задание 7.

Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

"""
with open('company_data.txt', 'r', encoding='utf-8') as f:
    companies_profit = {}
    average_profit = {}
    all_profit = 0
    profit_count = 0
    for line in f.readlines():
        data = line.rstrip().split()
        profit = float(data[2]) - float(data[3])
        companies_profit.update({data[0]: profit})
        if profit > 0:
            profit_count += 1
            all_profit += profit
average_profit.update({"average_profit": all_profit / profit_count})

with open('company_data.json', 'w+', encoding='utf-8') as f:
    json.dump([companies_profit, average_profit], f)
    f.seek(0)
    print(f.read())
    
