# Написать функцию проверки "Силы" пароля, возвращают всегда строку.
#  - если пароль короче 8 символов, то вернуть Too Weak.
#  - если пароль содержит только цифры, только строчные, только заглавные, то вернуть Weak.
#  - если пароль содержит символы любых 2х наборов, то вернуть Good.
#  - если пароль содержит символы любых 3х наборов, то вернуть Very Good.
import string


def password_str(value: str) -> str:
    short_password = len(value) < 8

    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(value) < 8:
        return 'Too Weak'
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return 'Weak'
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return 'Very Good'
    if (any(e in digits for e in value) and any(e in lowers for e in value)) or (
            any(e in digits for e in value) and any(e in uppers for e in value)) or (
            any(e in lowers for e in value) and any(e in uppers for e in value)):
        return 'Good'

# Альтернативный способ 1.
def password_str(value: str) -> str:
    short_password = len(value) < 8

    if short_password:
        return 'Too Weak'

    contains_numbers = any(map(str.isdigit, value))
    contains_lowers = any(map(str.islower, value))
    contains_upper = any(map(str.isupper, value))

    result = int(contains_numbers) + int(contains_lowers) + int(contains_upper)

    if result == 1:
        return 'Weak'
    elif result == 2:
        return 'Good'
    elif result == 3:
        return 'Very Good'


# Альтернативный способ 2.
def password_str(value: str) -> str:
    short_password = len(value) < 8

    if short_password:
        return 'Too Weak'

    contains_numbers = any(map(str.isdigit, value))
    contains_lowers = any(map(str.islower, value))
    contains_upper = any(map(str.isupper, value))

    password_levels = {1: 'Weak', 2: 'Good', 3: 'Very Good'}

    result = int(contains_numbers) + int(contains_lowers) + int(contains_upper)

    return password_levels[result]


if __name__ == '__main__':
    assert password_str('') == 'Too Weak'
    assert password_str('1234567') == 'Too Weak'
    assert password_str('qazwsxe') == 'Too Weak'
    assert password_str('QAZWSXE') == 'Too Weak'
    assert password_str('QAaa1') == 'Too Weak'
    assert password_str('12345678') == 'Weak'
    assert password_str('123456782340') == 'Weak'
    assert password_str('aqzwsxed') == 'Weak'
    assert password_str('aqzwsxedwed') == 'Weak'
    assert password_str('QAZWSXED') == 'Weak'
    assert password_str('QAZWSXEDDER') == 'Weak'
    assert password_str('1234qazww') == 'Good'
    assert password_str('1234qazwws') == 'Good'
    assert password_str('1234QAZW') == 'Good'
    assert password_str('1234QAZWQW') == 'Good'
    assert password_str('asdfQWER') == 'Good'
    assert password_str('asdfQWEREW') == 'Good'
    assert password_str('123qazQAZ') == 'Very Good'
    assert password_str('1234556Az') == 'Very Good'
    assert password_str('qazwsxedA1') == 'Very Good'
    assert password_str('QAZWSXED1a') == 'Very Good'
