# Эта программа демонстрирует, как прочитанные из файла
# числа конвертируются из строкового представления
# перед тем, как они используются в математической операции.

def main():
    # Открыть файл для чтения.
    infile = open('C:\Pandora\Sest.txt', 'r')

    # Прочитать 3 числа из файла.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Закрыть файл.
    infile.close()

    # сложить 3 числа.
    total = num3 + num2 + num1

    # Показать числа и их сумму.
    print('Числа: ', num1, num2, num3)
    print('Их сумма: ', total)

# Вызвать главную функцию
main()