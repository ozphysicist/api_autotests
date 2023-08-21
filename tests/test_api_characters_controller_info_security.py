from asserts import assert_equal, assert_in

from characters_controller.characters import CharactersController
from characters_controller.enums import ErrorMessages
from utilities.utils import (
    create_new_character_data_with_required_field,
    get_random_float,
    get_random_string_with_letters_digits,
)


def test_get_characters_status_without_authorization(
        characters: CharactersController,
) -> None:
    """
    Получение списка персонажей. Пользователь НЕ авторизован.
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
        'Фактическое описание описание ошибки {second} '
        'не содержит ожидаемую информацию {first}',
    )


def test_get_character_by_name_without_authorization(
        characters: CharactersController,
        character_name: str,
) -> None:
    """
    ППолучение данных по существующему персонажу. Пользователь НЕ авторизован.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    name = character_name
    response = characters.character_get(name=name, auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} '
        'не содержит ожидаемую информацию {first}',
    )


def test_create_new_character_without_authorization(
        characters: CharactersController,
) -> None:
    """
    Добавление персонажа, которого имя которого еще нет на сервере.
    Пользователь НЕ авторизован.
    Проверка корректности возращаемого статус кода и сообщения об ошибке.
    """
    data = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=get_random_string_with_letters_digits(6),
        other_aliases=get_random_string_with_letters_digits(7),
        universe=get_random_string_with_letters_digits(8),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_post(character=dict(data), auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} '
        'не содержит ожидаемую информацию {first}',
    )


def test_update_new_character_without_authorization(
        characters: CharactersController,
        character_name: str
) -> None:
    """
    Внесение изменений в данные о персонаже. Персонаж  существует.
    Пользователь НЕ авторизован.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    data = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=character_name,
        other_aliases=get_random_string_with_letters_digits(7),
        universe=get_random_string_with_letters_digits(8),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_put(character=dict(data), auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} '
        'не содержит ожидаемую информацию {first}',
    )


def test_delete_new_character_without_authorization(
        characters: CharactersController,
        character_name: str,
) -> None:
    """
    Удаление существующего персонажа. Пользователь НЕ авторизован.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    name = character_name
    response = characters.character_delete(name=name, auth=False)
    assert_equal(
        401,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.UNAUTHORIZED.value,
        response.text,
        'Фактическое описание описание ошибки {second} '
        'не содержит ожидаемую информацию {first}',
    )


def test_reset_characters_without_authorization(
        characters: CharactersController
) -> None:
    """
    Сброс коллекции в первоначальное состояние. Пользователь НЕ авторизован..
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
        'Фактическое описание описание ошибки '
        '{second} не содержит ожидаемую информацию {first}',
    )
