# Эта программа применяет цикл for для чтения
# всех значений из файла sales.txt.

def main():
    # Открыть файл sales.txt.
    sales_file = open('C:\Pandora\Sales.txt', 'r')

    # Прочитать все строки из файла.
    for line in sales_file:
        # Конвертировать строку в число с плавающей точкой.
        amount = float(line)
        # Отформатировать и показать сумму.
        print(format(amount, '.2f'))

    # Закрыть файл.
    sales_file.close()

# Запустить главную функцию.
main()