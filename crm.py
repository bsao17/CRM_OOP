class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = "") -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f"User(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, address={self.address})"

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_number}, {self.address})"


if __name__ == "__main__":
    from faker import Faker

    fake = Faker(locale="fr_FR")
    for _ in range(10):
        user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        print(user.__str__())
        print("-" * 10)
