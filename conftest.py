import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.sign_in_rozetka import SignInRozetka
from modules.ui.page_objects.delivery_count_page import DeliveryPage


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Olha"
        self.second_name = "Fedak"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api


@pytest.fixture
def database():
    db = Database()

    yield db


@pytest.fixture
def ui_rozetka():
    sign_in_page = SignInRozetka()
    sign_in_page.go_to()
    sign_in_page.try_login_modal()

    yield sign_in_page

    sign_in_page.close()


@pytest.fixture
def ui_delivery():
    delivery_page = DeliveryPage()
    delivery_page.go_to()
    delivery_page.close_add()

    yield delivery_page

    delivery_page.close()
