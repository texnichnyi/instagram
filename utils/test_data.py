import random


class TestUserData:
    @staticmethod
    def generate_unique_credentials():
        random_number = random.randint(2000, 10000)

        email = f"test_user_{random_number}@testdomain.com"
        username = f"new_user_{random_number}"
        full_name = "Test User"
        password = "qwerty123456!"

        return {
            'email': email,
            'username': username,
            'full_name': full_name,
            'password': password
        }

    @staticmethod
    def get_valid_login_credentials():
        return {
            'username': "test.yurii",
            'password': "qwerty123456"
        }
