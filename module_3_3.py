def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(a=13, b='v')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [4, 'Asdf', False]
value_dict = {'a': 5, 'b': 7, 'c': 9}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = [98.7, True]
print_params(*value_list_2, 77)
