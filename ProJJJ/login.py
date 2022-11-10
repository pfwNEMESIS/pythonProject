# Функция get_login_name применяет имя, фамилию
# и идентификационный номер в качестве аргументов.
# Она возвращает имя для входа в систему.

def get_login_name(first, last, idnumber):
    # Получить первые три буквы имени.
    # Если длина имени меньше 3х букв, то
    # срез вернет все имя целиком.
    set1 = first[0: 3]

    # Получить последние 3 буквы фамилии.
    # Если длинна фамилии меньше 3х символов, то
    # срез вернет всю фамилию целиком.
    set2 = last[0: 3]

    # Получить последние 3 буквы идентификатора.
    # Если длина идентификатора меньше 3х символов, то
    # срез вернет весь идентификатор.
    set3 = idnumber[-3:]

    # Собрать воедино наборы символов.
    login_name = set1 + set2 + set3

    # Вернуть имя для входа в систему.4
    return login_name


# Функция valid_password принимает пароль в
# качестве аргумента и возвращает истину либо ложь,
# сообщая о его допустимости или недопустимости. Допустимый
# пароль должен состоять как минимум из 7ми символов,
# иметь как минимум 1 символ в верхнем регистре,
# один символ в нижнем регистре и одну цифру.

def valid_password(password):
    # Назначить буквенным переменным значение False.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Запускаем валидацию.
    # Проверка длинны пароля.
    if len(password) >= 7:
        correct_length = True
    else:
        print('Пароль должен содержать не менее 7ми символов.'),
        return False

        # Проанализировать каждый символ и установить
        # соответствующий флаг, когда
        # требуемый символ найден.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
        if has_uppercase == False:
            print('Пароль должен содержать хотя бы 1 символ'
                  'в верхнем регистре.')
        if has_lowercase == False:
            print('Пароль должен содержать хотя бы 1 символ'
                  'в нижнем регистре.')
        if has_digit == False:
            print('Пароль должен содержать хотя бы 1 цифру.')

        # Определить, определены ли все требования.
        # Если это так, то назначить is_valid значение True.
        # В противном случае назначить is_valid значение False.4
        if correct_length and has_uppercase and \
                has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        # Вернуть переменную is_valid.
        return is_valid