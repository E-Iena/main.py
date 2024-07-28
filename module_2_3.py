my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0  # номер элемента из списка
k = len(my_list)  # последий элемент (конец) в списка
while n <= k:
    if my_list[n] > 0:
        print(my_list[n])
        n = n + 1
        continue
    elif my_list[n] == 0:
        n = n + 1
        continue
    else:
        break
print('нашли отрицательное')
