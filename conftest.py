import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


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
    # Personal Authorization
    """headers = {
        "Authorization": "Bearer N9soY5IC9IUwLuOu35qtrbtIU8jmmSySdU5Z3qHyt1CabMDjL3E5PxjkFYDaMLXdb_vTvU6UnYF-hudfgIfQ5g"
    }"""
    yield api


@pytest.fixture
def database():
    db = Database()

    yield db
