class BasePage:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f'Opening page: {self.name}')

    def close(self):
        print(f'Closing page: {self.name}')
