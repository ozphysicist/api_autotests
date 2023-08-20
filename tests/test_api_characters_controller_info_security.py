from characters_controller.characters import CharactersController
from characters_controller.enums import ErrorMessages
from utilities.utils import (
    create_new_character_data_with_required_field,
    get_exist_random_character_name,
    get_random_float,
    get_random_int,
    get_random_string_with_letters_digits,
)

from asserts import assert_equal, assert_in


def test_get_characters_status_without_authorization(characters: CharactersController) -> None:
    """
    Тест на получение списка персонажей без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    response = characters.characters_get(auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_get_character_by_name_without_authorization(characters: CharactersController) -> None:
    """
    Тест на получение существующего персонажа по имени без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    name = get_exist_random_character_name(controller=characters)
    response = characters.character_get(name=name, auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_create_new_character_without_authorization(characters: CharactersController) -> None:
    """
    Тест на создание нового персонажа без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    body = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=get_random_string_with_letters_digits(6),
        other_aliases=get_random_string_with_letters_digits(7),
        universe=get_random_string_with_letters_digits(8),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_post(character=dict(body), auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_update_new_character_without_authorization(characters: CharactersController) -> None:
    """
    Тест на обновление двнных существующего персонажа без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    body = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=get_exist_random_character_name(controller=characters, type_name='with_space'),
        other_aliases=get_random_string_with_letters_digits(7),
        universe=get_random_string_with_letters_digits(8),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_put(character=dict(body), auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_delete_new_character_without_authorization(characters: CharactersController) -> None:
    """
    Тест на удаление записи о существующем персонаже без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    name = get_exist_random_character_name(controller=characters)
    response = characters.character_delete(name=name, auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_reset_characters_without_authorization(characters: CharactersController) -> None:
    """
    Тест на сброс коллекции в первоначальное состояние без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    response = characters.reset_post(auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )
