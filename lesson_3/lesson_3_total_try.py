
# пользователи
print("Total list of Users:")
from lesson_3_task_1 import my_user1, my_user2
print("_________________________________")


# смартфоны
print("Total catalog of smartfones:")
from lesson_3_task_2 import catalog
print("_________________________________")

# адреса
print("Total list of mailing:")
from lesson_3_task_3 import mailing
print("_________________________________")


# отправитель, получатель, информация о посылке и адресах
print("Total information:")

print(f"Sender: {my_user1.first_name} {my_user1.last_name}, Recipient of the parcel: {my_user2.first_name} {my_user2.last_name}, Parcel item: {catalog[1].brand} {catalog[1].model}, Mailing details: from {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} to {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Total cost {mailing.cost} rubles.")
