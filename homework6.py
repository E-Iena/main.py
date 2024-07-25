#  словари
my_dict = {'Jane': 2007,
           'Elena': 1980,
           'Nataly': 1983,
           'Roma': 2000}
print('Словарь: ', my_dict)
print('Значение: ', my_dict['Jane'])  # по существующему ключу
print('Нет в словаре: ', my_dict.get('Maks'))  # по НЕ существующему ключу
my_dict.update({'Any': 2002,
                'Aleks': 2009})  # добавление
print('Обновленный словарь: ', my_dict)
del my_dict['Roma']  # удаление
print('Без одной пары: ', my_dict)  # без Ромы
b = my_dict.pop('Elena')
print('Значение удаленного ключа: ', b)
print("Окончательный словарь: ", my_dict)  # без Елены
print('****************************')
#  множества
my_set = {4, 2, 5.88, True, 'Jane', 5, (1, 2, 3), 'Jane'}
print("Множество: ", my_set)
my_set.add(0)
my_set.add(456)
print("Плюс два элемента: ", my_set)
my_set.remove(1)
print("Минус один элемент: ", my_set)
