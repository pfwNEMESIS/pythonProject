# позиционные аргументы всегда идут в начале! Позиционные БЕЗ присвоения(пример 1, 2, 3)
# / - всё что слева слэша - только позиционные аргументы.
# *, = всё, что справа - только keyword аргументы.
# *args собирает все позиционные аргументы в КОРТЕЖ!
# **kwargs собирает все keyword аргументы в СЛОВАРЬ!
# СПИСОК мы распаковываем через одну *
# СЛОВАРЬ распаковываем через две ** (**kwargs)

a, *b = 'abcd'


def example(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


def my_print(*args, **kwargs):
    print(f'Got keywords: {kwargs}')
    for arg in args:
        print(str(arg), **kwargs)


if __name__ == '__main__':
    # print(*[1, 2, 3])
    # example(1, 2, c=True, d=False)
    # my_print(1, 2, 3, 4, 5, sep=':', end='-')
    print(1, 2, **{'sep': ":", 'end': '-'})
    print(1, 2, sep=":", end='-')
# убрал комент
