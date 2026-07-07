class Address:

    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def print_address(self):
        print(f"{self.index}, {self.city},"
              f" {self.street}, {self.house} - {self.flat}")
