class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(f"First Name is {self.first_name}")

    def print_last_name(self):
        print(f"Last Name is {self.last_name}")

    def print_full_name(self):
        print(f"Full Name is {self.first_name} {self.last_name}")

