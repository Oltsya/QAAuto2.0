import pytest

from modules.ui.page_objects.sign_in_rozetka import SignInRozetka


@pytest.mark.uiroz
def test_wrong_email(ui_rozetka):
    with pytest.raises(AssertionError):
        ui_rozetka.try_login("123", "123")


@pytest.mark.uiroz
def test_without_email(ui_rozetka):
    with pytest.raises(AssertionError):
        ui_rozetka.try_login("", "123")


@pytest.mark.uiroz
def test_wrong_password(ui_rozetka):
    with pytest.raises(AssertionError):
        ui_rozetka.try_login("123@gmail.com", "111")


@pytest.mark.uiroz
def test_forgot_password(ui_rozetka):
    ui_rozetka.forgot_password("123@gmail.com")


@pytest.mark.uiroz
def test_sign_in_with_fb_clickable(ui_rozetka):
    ui_rozetka.sign_in_with_other_app(
        "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/div/div/rz-social-auth/button[1]",
        "Facebook - Google Chrome",
    )


@pytest.mark.uiroz
def test_sign_in_with_google_clickable(ui_rozetka):
    ui_rozetka.sign_in_with_other_app(
        "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/div/div/rz-social-auth/button[2]",
        "Sign in - Google Accounts - Google Chrome",
    )


@pytest.mark.uiroz
def test_sign_in_as_new_user_modal(ui_rozetka):
    ui_rozetka.sign_in_as_new_user()
