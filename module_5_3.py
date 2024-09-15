class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range((new_floor) + 1):
                print(f' этаж {i}')
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors} '

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    # увеличивает кол-во этажей на переданное значение value (объект + value)
    def __add__(self, value):
        if not isinstance(value, int):
            print(f'Значение {value} не подходит, нужно целое число')
        else:
            self.number_of_floors = self.number_of_floors + value
        return self

    # увеличивает кол-во этажей на переданное значение value (value + объект)
    def __radd__(self, value):
        if not isinstance(value, int):
            print(f'Значение {value} не подходит, нужно целое число')
        else:
            self.number_of_floors = self.number_of_floors + value
        return self

    # увеличивает кол-во этажей на переданное значение value (+=)
    def __iadd__(self, value):
        if not isinstance(value, int):
            print(f'Значение {value} не подходит, нужно целое число')
        else:
            self.number_of_floors = self.number_of_floors + value
        return self


h1 = House('ЖК Эльбрус', 15)
h2 = House('ЖК Акация', 5)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h1)  # __str__
print(h2)  # __str__
print(len(h1))  # __len__
print(len(h2))  # __len__
print('****************')
print(f'h1 == h2 {h1 == h2}')  # __eq__
print(f'h1 < h2 {h1 < h2}')  # __lt__
print(f'h1 <= h2 {h1 <= h2}')  # __le__
print(f'h1 > h2 {h1 > h2}')  # __gt__
print(f'h1 >= h2 {h1 >= h2}')  # __ge__
print(f'h1 != h2 {h1 != h2}')  # __ne__
print('****************')

h1 = h1 + (0.3)  # __add__ сложение
print(f'add - {h1}')
print(h1 == h2)

h2 = 8 + h2  # __radd__ сложение
print(f'radd - {h2}')

h1 += 3  # __iadd__  сложение
print(f'iadd - {h1}')
