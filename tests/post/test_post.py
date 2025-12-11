import pytest

from utils.test_data import TestUserData


@pytest.mark.posts
def test_user_can_like_post(login_page):
    credentials = TestUserData.get_valid_login_credentials()

    home_page = login_page.login(
        credentials['username'],
        credentials['password']
    )

    all_posts = home_page.get_all_posts()
    first_post = all_posts[0]
    first_post.click_like()

    assert first_post.is_liked(), "Перший пост не було лайкнуто."


@pytest.mark.posts
def test_scroll_to_posts_bottom(login_page):
    credentials = TestUserData.get_valid_login_credentials()

    home_page = login_page.login(
        credentials['username'],
        credentials['password']
    )
    target_locator = home_page.bottom_panel.HOME_BUTTON
    is_bottom_reached = home_page.scroll_to_element(target_locator)

    assert is_bottom_reached, "Ви недоскролили до низу сторінки."


@pytest.mark.posts
def test_carusel_post_click_next_and_previous(login_page):
    credentials = TestUserData.get_valid_login_credentials()

    home_page = login_page.login(
        credentials['username'],
        credentials['password']
    )
    carusel_post = home_page.get_post_by_author('selenagomez')

    assert carusel_post.click_next_photo(), "Ви не клікнули наступне фото."
    assert carusel_post.click_previous_photo(), "Ви не клікнули попереднє фото."
