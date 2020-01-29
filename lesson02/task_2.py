"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
user_list = []

while True:
    user_el = input('Введите новый элемент списка. Если достаточно, просто нажмите Enter: ')
    if not user_el:
        break
    user_list.append(user_el)
    if not user_list.index(user_el) % 2:
        user_list[user_list.index(user_el)], user_list[user_list.index(user_el) - 1] = user_list[user_list.index(user_el) - 1], user_list[user_list.index(user_el)]
print(user_list)
