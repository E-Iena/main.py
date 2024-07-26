grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#  с оценками
print('Оценок ', len(grades), ' штук')
grades = [sum(grades[0]) / len(grades[0]),
          sum(grades[1]) / len(grades[1]),
          sum(grades[2]) // len(grades[2]),
          sum(grades[3]) // len(grades[3]),
          sum(grades[4]) // len(grades[4])]
print('Список средних баллов: ', grades)
#  с именами
print('Имен - ', len(students))
students = sorted(students)
print('Список имен по алфавиту: ', students)
print('**********************************')
print({students[0]: grades[0]}, '\n',  # вывод данных на новой строке
      {students[1]: grades[1]}, '\n',
      {students[2]: grades[2]}, '\n',
      {students[3]: grades[3]}, '\n',
      {students[4]: grades[4]})
print('**********************************')
spisok = {(students[0]): grades[0], (students[1]): grades[1], (students[2]): grades[2], (students[3]): grades[3],
          (students[4]): grades[4]}  # создание "словаря"
print('Решение по заданию средний балл: ', '\n', spisok)
print(type(spisok))  # проверка: класс dict
