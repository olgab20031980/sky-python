from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Tverskaya", "15", "42")
from_address = Address("654321", "Saint Petersburg", "Nevsky", "10", "5")

mailing = Mailing(to_address, from_address, 500, "ABC123456")

mailing.print_info()
