import pytest

from utils.test_data import TestUserData


@pytest.mark.signup
def test_successful_new_user_registration(sign_up_page):
    user_data = TestUserData.generate_unique_credentials()

    birthday_form = sign_up_page.sign_up_new_user(
        email_or_phone=user_data['email'],
        full_name=user_data['full_name'],
        username=user_data['username'],
        password=user_data['password']
    )
    assert birthday_form
