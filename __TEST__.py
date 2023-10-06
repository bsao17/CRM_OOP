import pytest

from crm import User


class TestUser:
    """
    Creates a new user with valid first and last names.

    This function initializes a new User object with the given first and last names.
    It then asserts that the user's first name is set to "John", the last name is set to "Doe",
    the phone number is empty, and the address is empty.

    Parameters:
    - self: The current instance of the test class.

    Returns:
    - None
    """
    #  Create a User object with valid first_name and last_name.
    def test_create_user_with_valid_names(self):
        user = User("John", "Doe")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.phone_number == ""
        assert user.address == ""

    """
    Test case for creating a user with valid details.

    This test case verifies that a user object is created correctly when valid details are provided.
    It creates a user object using the User class with the following details:
    - First name: "John"
    - Last name: "Doe"
    - Phone number: "1234567890"
    - Address: "123 Main St"

    The test asserts the following conditions:
    - The first name of the user object is "John".
    - The last name of the user object is "Doe".
    - The phone number of the user object is "1234567890".
    - The address of the user object is "123 Main St".

    This test case is part of the unit tests for the User class.

    Returns:
    None
    """
    #  Create a User object with valid first_name, last_name, phone_number, and address.
    def test_create_user_with_valid_details(self):
        user = User("John", "Doe", "1234567890", "123 Main St")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.phone_number == "1234567890"
        assert user.address == "123 Main St"
