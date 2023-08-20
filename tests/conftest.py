from characters_controller.characters import CharactersController
from characters_controller.enums import ServiceDBLimits
from utilities.utils import (
    create_new_character_data_with_required_field,
    get_random_float,
    get_random_string_with_letters_digits,
)
from vars import envars

import pytest


@pytest.fixture()
def characters() -> CharactersController:
    """Фикстура, вызывающая экземпляр класса Characters"""
    return CharactersController(
        base_url=envars.SERVICE_BASE_URL,
        user_login=envars.SERVICE_LOGIN,
        user_password=envars.SERVICE_PASSWORD,
    )


@pytest.fixture()
def fill_db_to_max_recs(characters: CharactersController) -> None:
    """
    Фикстура, заполняющая БД до максимального количества записей или максимального - 1 запись.
    :param: rec_count: количество записей, до которого нужно заполнить БД
    :return: None
    """
    empty_db_rec_counts = ServiceDBLimits.MAX_DB_RECORDS.value - len(characters.characters_get().json()['result'])
    for record in range(empty_db_rec_counts):
        data = create_new_character_data_with_required_field(
            education=get_random_string_with_letters_digits(10),
            height=get_random_float(),
            identity=get_random_string_with_letters_digits(10),
            name=get_random_string_with_letters_digits(10),
            other_aliases=get_random_string_with_letters_digits(10),
            universe=get_random_string_with_letters_digits(10),
            weight=get_random_float(before_dot=2, after_dot=1)
        )
        characters.character_post(character=dict(data))

    yield

    characters.reset_post()


@pytest.fixture()
def character_name(characters: CharactersController) -> str:
    data = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=get_random_string_with_letters_digits(10),
        other_aliases=get_random_string_with_letters_digits(10),
        universe=get_random_string_with_letters_digits(10),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_post(character=dict(data))
    name = response.json()['result']['name']

    yield name

    characters.reset_post()
