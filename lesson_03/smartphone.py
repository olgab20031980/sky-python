class Smartphone:

    def __init__(self, brend, model, number):
        self.brend = brend
        self.model = model
        self.number = number

    def print_info(self):
        print(f"{self.brend}, {self.model}, {self.number}")
