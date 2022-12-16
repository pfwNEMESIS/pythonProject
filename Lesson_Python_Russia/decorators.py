# Функция - полноправный объект.
# Внутренняя функция может захватывать переменные из внешней..


def logger(func):
    def wrapper(a, b):
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} finished')
        return result

    return wrapper  # МЫ не вызываем wrapper, мы возвращаем его самого.


@logger
def summ(a, b):  # в этот момент summ=wrapper
    return a + b


if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))

    # print(logger(summ)(2, 3))

    # summ = logger(summ)
    # print(summ(2, 3))

    print(summ)
