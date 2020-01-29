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
    el_index = len(user_list) - 1
    if el_index % 2:
        user_list[el_index], user_list[el_index - 1] = user_list[el_index - 1], user_list[el_index]
print(user_list)
