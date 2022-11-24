import pprint

# List comprehension = listcomps
# Generator expression = genexp
# читается слева направо.
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВЫВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# Нельзя делать больше 2х for в одной строке[].


text = 'hello world'
words = [word.capitalize() for word in text.split()]  # только преобразовываем

ints = [-1, 2, 0, 3, -4]
positives = [e for e in ints if e > 0]  # только фильтруем

squares = [e * e for e in range(10) if e % 2 == 0]  # и фильтруем и преобразовываем

squares2 = []
for e in range(10):
    if e % 2 == 0:
        squares2.append(e * e)

letters = [letter for word in text.split() for letter in word if letter > 'l']

matrix = [list(range(x, x + 3)) for x in range(3)]

if __name__ == '__main__':
    pprint.pprint(matrix, indent=1, width=15)
