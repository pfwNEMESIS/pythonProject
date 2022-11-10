# Эта программа показывает пошаговые инструкции
# для разборки бельевой сушилки Acme.
def main():
    # Показать стартовое сообщение
    startup_message()
    input('Нажать Enter, чтобы увидеть шаг 1.')
    # Показать шаг 1.
    step1()
    input('Нажмите Enter, чтобы увидеть шаг 2.')
    # Показать шаг 2.
    step2()
    input('Нажмите Enter, чтобы увидеть шаг 3.')
    # Показать шаг 3.
    step3()
    input('Нажмите Enter, чтобы показать шаг 4.')
    # Показать шаг 4.
    step4()

# Функция Startup_message показывает
# первоначальное сообщение
def startup_message():
    print('Эта программа даёт рекомендации')
    print('по разборке бельевой сушилки')
    print('Данный процесс состоит из 4х шагов.')
    print()

# Функция step1 показывает инструкции для шага 1.
def step1():
    print('Шаг1: отключить сушилку и ')
    print('отодвинуть ее от стены.')
    print()

# Функция step2 показывает инструкции для шага 2.
def step2():
    print('Шаг 2: Удалить 6 винтов')
    print('с задней стороны сушилки.')
    print()

# Функция step3 показывает инструкции для шага 3.
def step3():
    print('Шаг 3: удалите заднюю панель сушилки.')
    print()

# Функция step4 показывает инструкции для шага 4.
def step4():
    print('Шаг 4: Вынуть верхний блок сушилки.')
    print()

# Вызвать главную функцию, чтобы начать программу.
main()