# Эта программа добавляет записи о запасах кофе
# в файл coffee.txt.

def main():
    # Создать переменную для управления циклом.
    another = 'д'

    # Открыть файл coffee.txt в режиме дозаписи.
    coffee_file = open('C:\Pandora\coffee.txt', 'a')

    # Добавить запись в файл.
    while another == 'д' or another == 'Д':
        # Получить данные с записью о кофе.
        print('Введте следующие данные о кофе:')
        descr = input('Описание: ')
        qty = int(input('Количество (в фунтах): '))

        # Добавить данные в файл.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Определить, желает ли пользователь добавить
        # в файл ещё одну запись.
        print('Желаете ли Вы добавить ещё одну запись? ')
        another = input('Д = да, всё остальное = нет: ')

    # Закрыть файл.
    coffee_file.close()
    print('Данные добавлены в coffee.txt.')

# Вызвать главную функцию.
main()