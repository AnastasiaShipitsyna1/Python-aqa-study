from smartphone import Smartphone


catalog = [
        Smartphone("Samsung", "Galaxy S21", "+79123456789"),
        Smartphone("Apple", "iPhone 13", "+79234567890"),
        Smartphone("Google", "Pixel 6", "+79345678901"),
        Smartphone("OnePlus", "9 Pro", "+79456789012"),
        Smartphone("Xiaomi", "Mi 11", "+79567890123")
    ]

for phone in catalog:
        print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
