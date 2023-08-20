import pytest

from characters_controller.characters import CharactersController
from vars import envars


@pytest.fixture()
def characters() -> CharactersController:
    """Фикстура, вызывающая экземпляр класса Characters"""
    return CharactersController(
        base_url=envars.SERVICE_BASE_URL,
        user_login=envars.SERVICE_LOGIN,
        user_password=envars.SERVICE_PASSWORD,
    )
