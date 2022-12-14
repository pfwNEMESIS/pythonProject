# Эта программа получает серию оценок за лабораторные
# работы и вычисляет среднюю оценку,
# отбрасывая самую низкую.

def main():
    # Получить от пользователя оценки.
    score = get_score()

    # Вычислить сумму оценок.
    total = get_total(score)

    # Получить самую низкую оценку.
    lowest = min(score)

    # Вычислить самую низкую оценку.
    total -= lowest

    # Вычислить среднюю оценку. Обратите внимание, что
    # мы делим на количество оценок минус 1, потому то
    # самая низкая оценка была отброшена.

    average = total / (len(score) - 1)

    # Показать среднее значение.
    print('Средняя оценка с учётом отброшенной',
          'самой низкой оценкой составляет:', average)
# Функция get_score получает от пользователя
# серию оценок и сохраняет их в списке.
# Указания функция возвращает ссылку на список.
def get_score():
    # Создаём пустой список.
    test_score = []

    # Создаём переменную для управления циклом.
    again = 'д'

    # Получить от пользователя оценки и добавить их
    # в список.
    while again == 'д':
        # Получить оценку и добавить ее в список.
        value = float(input('Введите оценку: '))
        test_score.append(value)

        # Желаете проделать ещё раз?
        print('Желаете добавить ещё одну оценку?')
        again = input('д = да, всё остальное = нет: ')
        print()

    # Вернуть список.
    return test_score

# Функция get_total принимает список в качестве
# аргумента и возвращает сумму значений
# в списке.
def get_total(value_list):
    # Создать переменную для применения в качестве накопителя.
    total = 0.0

    # Вычислить сумму значений элементов списка.
    for num in value_list:
        total += num

    # Вернуть сумму.
    return total

# Вызвать главную функцию.
main()