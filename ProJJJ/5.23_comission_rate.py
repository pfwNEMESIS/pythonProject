# Эта программа вычисляет выплату продавцу
# в компании "Делай свою музыку".
def main():
    # Получить сумму продаж.
    sales = get_sales()

    # Получить сумму авансовой оплаты.
    advanced_pay = get_advanced_pay()

    # Определить ставку комиссионных.
    comm_rate = determine_comm_rate(sales)

    # Расчитать оплату.
    pay = sales * comm_rate - advanced_pay

    # Показать сумму выплаты.
    print('Выплата составляет $', format(pay, '.2f'), sep='')

    # Определить, является ли выплата отрицательной.
    if pay < 0:
        print('продавец должен возместить разницу')
        print('компании.')

# Функция get_sales получает от пользователя
# месячные продажи продавца т возвращает это значение.

def get_sales():
    # Получить сумму месячных продаж.
    monthly_sales = float(input('Введите сумму месячных продаж: '))

    # Вернуть введенную сумму.
    return monthly_sales

# Функция get_advanced_pay получает сумму
# авансовой выплаты конкретному продавцу
# и возвращает эту сумму.
def get_advanced_pay():
    # Получить сумму авансовой выплаты.
    print('Введите сумму авансовой выплаты либо')
    print('введите 0, если такой выплаты не было.')
    advanced = float(input('Авансовая выплата: '))

    # Вернуть авансовую выплату.
    return advanced

# Функция determine_comm_rate принимает сумму продаж
# в качестве аргумента и возвращает подходящую
# ставку комиссионных.
def determine_comm_rate(sales):
    # Определить ставку комиссионных
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Вернуть ставку комиссионных.
    return rate

# Вызвать главную программу.
main()