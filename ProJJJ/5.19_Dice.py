# Эта программа бросает кубики.
import random

# Минимальные и максимальные значения кубиков.
MIN = 1
MAX = 6

def main():
    # Создать переменную, которая управляет циклом.
    again = 'д'

    # Имитировать бросание кубиков.
    while again == 'д' or again == 'Д':
        print('Бросаем кубики...')
        print('Значение граней: ')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Сделать ещё один бросок?
        again = input('Бросить ещё раз? (д = да): ')

# Вызвать главную функцию.
main()