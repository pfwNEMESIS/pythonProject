class ArgumentEqualZeroError(Exception):
    """Выбрасывается, когда делитель равен нулю"""
    pass


class ArgumentIsNotInteger(Exception):
    """Выбрасывается, когда аргумент не целое число"""


def divide(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentIsNotInteger("Аргументы должны быть целыми числами")
    if b == 0:
        raise ArgumentEqualZeroError("Делитель не может быть равен 0")

    return a // b


if __name__ == '__main__':
    try:
        result = divide(4, 0)
    except (ArgumentIsNotInteger, ArgumentEqualZeroError) as exc:
        print(exc)
    finally:
        print('Finish')
