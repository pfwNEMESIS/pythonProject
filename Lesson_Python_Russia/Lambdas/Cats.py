class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat{self.name}, age is {self.age}"


if __name__ == '__main__':
    cats = [Cat('Tom', 4), Cat('Angela', 3)]
    print(sorted(cats, key=lambda cat: cat.name))
