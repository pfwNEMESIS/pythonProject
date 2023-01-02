class Resource:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f"Resource was opened with arguments {args}")
        self.opened = True

    def close(self):
        print(f"Resource was closed!")
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Memory leak detected! Resource was not closed!')

    def action(self):
        print('Do something with resource')


if __name__ == '__main__':
    pass