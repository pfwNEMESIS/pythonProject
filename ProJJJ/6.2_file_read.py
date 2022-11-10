# Эта программа читает и показывает содержимое
# файла test.txt.
def main():
    # Открыть файл с именем text.txt
    infile = open('C:\Pandora\Sest.txt', 'r')

    # Прочитать содержимое файла.
    file_contents = infile.read()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, считанные
    # в оперативную память.
    print(file_contents)

# Вызвать главную функцию.
main()