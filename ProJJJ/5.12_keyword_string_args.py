# Эта программа демонстрирует передачу в функцию
# двух строковых значений в качестве именованных аргументов.

def main():
    first_name = input('Введите своё имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Вае имя в обратном порядке')
    revers_name(last=last_name, first=first_name)

def revers_name(first, last):
    print(last, first)

# Вызвать главную функцию.
main()