# Эта программа позволяет пользователю производить поиск
# в файле coffee.txt

def main():
    # Создать булевую переменную для использования ее в качестве флага.
    found = False

    # Получить искомое значение.
    search = input('Поиск: ')

    # Открыть файл coffee.txt.
    coffee_file = open('C:\Pandora\coffee.txt', 'r')

    # Прочитать поле с описанием кофе первой записи.
    descr = coffee_file.readline()

    # прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Определить, соответствует ли запись
        # поисковому значению.
        if descr == search:
            # показать запись.
            print('Описание: ', descr)
            print('Количество: ', qty)
            print()

            # Назначить флагу found True
            found = True

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл.
    coffee_file.close()

    # Если поисковое значение в файле не найдено,
    # то показать сообщение.
    if not found:
        print('Это значение не найдено.')

# Вызвать главную функцию.
main()
