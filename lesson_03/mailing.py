class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost  # int
        self.track = track  # str

    def print_info(self):
        print(f"Отправление: {self.track}")
        print("От кого:")
        self.from_address.print_address()
        print("Кому:")
        self.to_address.print_address()
        print(f"Стоимость: {self.cost} рублей.")
