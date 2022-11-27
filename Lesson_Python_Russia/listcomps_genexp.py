import pprint

# List comprehension = listcomps
# Generator expression = genexp

# Читается слева направо.
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВЫВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# Нельзя делать больше 2х for в одной строке[].
# Для словаря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ (двоеточие)
# Genexp. Генератор не формирует структуру данных,
# как это делают ...comps, он формирует ОБЪЕКТ генератора.
# Генератор вернёт объект, а не коллекцию
# Генератор ленивый, не выполняется и не занимает память, пока не потребуется.
# Генератор проверяет источник при создании!!!
# Генератор одноразовый, если исчерпан, то бросает StopIteration.
# Цикл for перехватывает StopIteration.
# Используйте genexp вместо comps, кроме случаев, когда len или индексы (3, 5, 6 элемент и тд.)

from time import sleep

text = 'hello world'
words = [word.capitalize() for word in text.split()]  # только преобразовываем

ints = [-1, 2, 0, 3, -4]
positives = [e for e in ints if e > 0]  # только фильтруем

squares = [e * e for e in range(10) if e % 2 == 0]  # и фильтруем и преобразовываем

squares2 = []
for e in range(10):
    if e % 2 == 0:
        squares2.append(e * e)

matrix = [list(range(x, x + 3)) for x in range(3)]

# Listcomps
letters = [letter for word in text.split() for letter in word if letter > 'l']

# Setcomps, создаёт 'множества'.
unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

# Dictcomps. Словарь.
alphabet = {index: letter for index, letter in enumerate('absdifghijklnopqrstuvwxyz', 1)}

# Genexp. Генератор не формирует структуру данных, как это делают ...comps
# он формирует ОБЪЕКТ генератора.
positives_gen = (e for e in ints if e > 0)


def some_sourse():
    # open db
    # read file
    # calculate
    return 1, 2, 3

def some_filter(x):
    sleep(1)
    return True

def some_mapping(x):
    sleep(1)
    return x

if __name__ == '__main__':
    it = (some_mapping(e) for e in some_sourse() if some_filter(e))
    print(next(it))