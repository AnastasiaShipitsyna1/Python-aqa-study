from decimal import Decimal
from address import Address
from mailing import Mailing



to_address = Address("12345", "Suva", "Bula", "lot 55", "55")
from_address = Address("54321", "Nadi", "Vinaka", "lot 3", "12")

mailing = Mailing(to_address, from_address, "100.50", "TRACK123")

print(f"Send {mailing.track} from {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} to {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Total cost {mailing.cost} rubles.")
