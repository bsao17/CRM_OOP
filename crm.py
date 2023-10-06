class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = "") -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    """
    Returns the full name of the person.

    :return: (str) The full name of the person.
    """
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    """
    Return a string representation of the User object.
    """
    def __repr__(self):
        return (f"User(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, "
                f"address={self.address})")

    """
    Returns a string representation of the object.

    :return: A string containing the first name, last name, phone number, and address of the object.
    :rtype: str
    """
    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address})"


if __name__ == "__main__":
    from faker import Faker

    fake = Faker(locale="fr_FR")
    for _ in range(10):
        user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        print(str(user))
        print("-" * 10)

