# Эта программа показывает записи, которые
# находятся в файле employees.txt.

def main():
    # Открыть файл employees.txt.
    emp_file = open('C:\Pandora\employees.txt', 'r')

    # Прочитать первую строку в файл, т.е.
    # поле с именем сотрудника первой записи.
    name = emp_file.readline()

    # Если прочитано, то продолжить обработку.
    while name != '':
        # Прочитать поле с идентификационным номером.
        id_num = emp_file.readline()

        # Прочитать поле с названием отдела.
        dept = emp_file.readline()

        # Удалить символы новой строки из полей.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Показать запись.
        print('Имя: ', name)
        print('ИД: ', id_num)
        print('Отдел: ', dept)
        print()

        # Прочитать поле с именем следующей записи.
        name = emp_file.readline()

    # Закрыть файл.
    emp_file.close()

# Вызвать главную функцию.
main()