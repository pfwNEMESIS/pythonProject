# Эта программа показывает записи из файла coffee.tx.

def main():
    coffee_file = open('C:\Pandora\coffee.txt', 'r')

    # Прочитать поле с описанием первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Показать запись.
        print('Описание:', descr)
        print('Количество:', qty)

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл.
    coffee_file.close()

# Вызвать главную функцию.
main()
