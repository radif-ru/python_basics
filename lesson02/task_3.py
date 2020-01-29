"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

get_month = input('Введите месяц в виде целого числа от 1 до 12: ')
get_month = int(get_month) if get_month.isdigit() else 0

# решение с помощью list:
months_list = ['зима', 'весна', 'лето', 'осень']

if (0 < get_month < 3) or get_month == 12:
    print(months_list[0])
elif 2 < get_month < 6:
    print(months_list[1])
elif 5 < get_month < 9:
    print(months_list[2])
elif 8 < get_month < 12:
    print(months_list[3])
else:
    print('Введены некорректные данные')

# решение с помощью dict:
months_dict = {'зима': {12, 1, 2}, 'весна': set(range(3, 6)), 'лето': set(range(6, 9)), 'осень': set(range(9, 12))}

for key, value in months_dict.items():
    if get_month in value:
        print(key)
