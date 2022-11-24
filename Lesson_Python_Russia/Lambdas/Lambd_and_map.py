# Аналог def!! ()
# Можно писать всё что допустимо после return в def
# Не выполняется до вызова.
from operator import attrgetter, itemgetter


def square(x):
    return x ** 2


def is_even(x):
    return x % 2 == 0


any_ = lambda: abracadabra
any2 = lambda: square(use(it))


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat{self.name}, age is {self.age}"


if __name__ == '__main__':
    ints = list(range(10))
    print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, ints))))
    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}  # ('a',3)
    print(sorted(a_dict.items(), key=lambda x: x[1]))
    cats = [Cat('Tom',2), Cat('Angela',3)]
    print(sorted(cats, key=lambda cat: cat.age))
