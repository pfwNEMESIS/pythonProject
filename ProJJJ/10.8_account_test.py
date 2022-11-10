# Эта программа демонстрирует класс BankAccount.

import bankaccount

def main():
    # Получаем начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount
    savings = bankaccount.BankAccount(start_bal)

    # Внести на счёт заработную плату пользователя.
    pay = float(input('Сколько вы получили на этой неделе? '))
    print('Вношу', pay,'руб. на Ваш счёт.')
    savings.deposit(pay)

    # Показать остаток.
    print('Ваш остаток на банковском счёте состаляет ',
          format(savings.get_balance(), '.2f'), sep='')

    # Получить сумму для снятия с банковского счёта.
    cash = float(input('Какую сумму Вы желаете снять со счёта? '))
    print('Снимаю', cash,'руб. с Вашего счёта. ')
    savings.withdraw(cash)

    # Показать остаток.
    print('Ваш остаток на банковском счёте составляет ',
          format(savings.get_balance(), '.2f'), sep='')

# Вызвать главную функцию.
main()