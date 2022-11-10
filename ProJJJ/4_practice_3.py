# Эта программа подсчитывает расходы за месяц.

# Инициализируем накапливающую переменную.
total = 0

# Просим пользователя ввести месячный бюджет.
month = int(input('Введите выделенную сумму на месяц: '))
pay = int(input('Сколько было трат в этом месяце? '))

# Вводим отдельные статьи бюджета.
for counter in range(pay):
    number = int(input('Введите сумму покупки: '))
    #num1 = int(input('Коммунальные услуги:'))
    #num2 = int(input('Счётчики: '))
    #num3 = int(input('Другое: '))
    total = total + number

if total > month:
    score = total - month
    print('Вы превысили месячный бюджет на', score)
else:
    score = month - total
    print('В этом месяце Вы остались в плюсе на', score)