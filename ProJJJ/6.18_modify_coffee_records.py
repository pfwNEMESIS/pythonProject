# Эта программа позволяет пользователю изменять количество
# в записи файла coffee.txt.

import os  # Этот модуль нужен для функций remove и rename.

def main():
    # Создать булевую переменную для использования ее в качестве флага.
    found = False

    # Получать искомое значение и новое количество.
    search = input('Введите искомое описание: ')
    new_qty = int(input('Введите новое количество: '))

    # Открыть исходный файл coffee.txt.
    coffee_file = open('C:\Pandora\coffee.txt', 'r')

    # Открыть временный файл.
    temp_file = open('C:\Pandora\list_temp.txt', 'w')

    # Прочитать поле с описанием первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Записать во временный файл измененную запись,
        # либо новую запись, если эта запись
        # подлежит изменению.
        if descr == search:
            # Записать во временный файл измененную запись.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

            # Назначить флагу found значение True.
            found = True
        else:
            # Записать во временный файл исходную запись.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        # прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть исходный файл.
    coffee_file.close()
    temp_file.close()

    # Удалить исходный файл coffee.txt.
    os.remove('C:\Pandora\coffee.txt')

    # Переименовать временный файл.
    os.rename('C:\Pandora\list_temp.txt', 'C:\Pandora\coffee.txt')

    # Если искомое значение в файле не найдено,
    # то показать сообщение.
    if found:
        print('Файл обновлен.')
    else:
        print('Это значение в файле не найдено.')

# Вызвать главную функцию.
main()
