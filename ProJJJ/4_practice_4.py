# Программа для подсчёта пройденного расстояния.

# Просим ввести значения.
speed = int(input('С какой скоростью едет авто км/ч? '))
time_to_ride = int(input('Сколько по времени оно двигалось? '))

# Печатаем заголовок таблицы.
print('Час\tПройденное расстояние')
print('--------------------------')

# Расчёт скорости и вывод результатов.
for time_to_ride in range(1, time_to_ride):
    distance = speed * time_to_ride
    print(time_to_ride, '\t', distance)