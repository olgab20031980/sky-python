from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Note 10", "+7910555-55-55"),
    Smartphone("Samsung", "Note 10 Plus", "+7960333-33-33"),
    Smartphone("iPhone", "17 Pro Max", "+7900999-99-99"),
    Smartphone("iPhone", "17 Pro", "+7950880-88-88"),
    Smartphone("Samsung", "S22 Ultra", "+7910777-77-77"),
]

for phone in catalog:
    phone.print_info()
