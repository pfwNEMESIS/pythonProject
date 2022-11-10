# Эта программа получает имя и фамилию пользователя
# и id-номер студента. На основе этих данных
# она генерирует имя для входа в систему.

import login

def main():
    # Получить имя, фамилию, id пользователя.
    first = input('Введите своё имя: ')
    last = input('Введите свою фамилию: ')
    idnumber = input('Введите свой id-номер: ')

    # получить имя для входа в систему.
    print('Ваше имя для входа в систему:')
    print(login.get_login_name(first, last, idnumber))

# Вызвать главную функцию.
main()