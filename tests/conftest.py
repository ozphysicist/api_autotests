import pytest

from characters_controller.characters import Characters


@pytest.fixture()
def characters() -> Characters:
    """Фикстура, вызывающая экземпляр класса Characters"""
    return Characters()