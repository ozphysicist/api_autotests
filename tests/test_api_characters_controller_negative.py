from typing import Callable

from characters_controller.characters import CharactersController
from characters_controller.enums import ErrorMessages, ServiceDBLimits
from utilities.utils import (
    create_new_character_data_with_required_field,
    create_new_character_data_without_required_field,
    create_new_character_data_with_wrong_data_type,
    get_exist_random_character_name,
    get_random_string_with_letters_digits,
    get_random_float,
    get_random_int,
)
from asserts import assert_equal, assert_in


def test_get_non_exist_character_by_name(characters: CharactersController) -> None:
    """
    Тест на получение существующего персонажа по имени без авторизации.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    name = get_random_string_with_letters_digits(6)
    response = characters.character_get(name=name)
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.NO_SUCH_NAME.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_create_new_character_without_required_field(characters: CharactersController) -> None:
    """
    Тест на создание записи о новом персонаже. В теле запроса отсутсвует обязательное поле name
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    data = create_new_character_data_without_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        other_aliases=get_random_string_with_letters_digits(7),
        universe=get_random_string_with_letters_digits(8),
        weight=get_random_float(before_dot=2, after_dot=1),
    )
    response = characters.character_post(character=dict(data))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.MISSING_REQUIRED_FIELD.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_create_character_with_exist_name(characters: CharactersController, character_name: str) -> None:
    """
    Тест на создание записи о персонаже, имя (значение поля name) уже существет (есть в БД).
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    data = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=character_name,
        other_aliases=get_random_string_with_letters_digits(7),
        universe=get_random_string_with_letters_digits(8),
        weight=get_random_float(before_dot=2, after_dot=1),
    )
    response = characters.character_post(character=dict(data))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.ALREADY_EXIST.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_create_character_with_wrong_field_data_type(characters: CharactersController) -> None:
    """
    Тест на создание записи о персонаже, поля в теле запроса имеют неверный тп данных.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    data = create_new_character_data_with_wrong_data_type(
        education=get_random_int(10),
        height=get_random_float(),
        identity=get_random_int(10),
        name=get_random_string_with_letters_digits(10),
        other_aliases=get_random_int(10),
        universe=get_random_int(10),
        weight=get_random_float(),
    )
    response = characters.character_post(character=dict(data))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.NOT_A_VALID_STRING.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_create_character_with_351_characters_in_string_fields(characters: CharactersController) -> None:
    """
    Тест на создание записи о персонаже, имя (значение поля name) уже существет (есть в БД).
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    data = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(ServiceDBLimits.STRING_FIELD_DATA_LIMIT.value + 1),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(ServiceDBLimits.STRING_FIELD_DATA_LIMIT.value + 1),
        name=get_exist_random_character_name(controller=characters),
        other_aliases=get_random_string_with_letters_digits(ServiceDBLimits.STRING_FIELD_DATA_LIMIT.value + 1),
        universe=get_random_string_with_letters_digits(ServiceDBLimits.STRING_FIELD_DATA_LIMIT.value + 1),
        weight=get_random_float(before_dot=2, after_dot=1),
    )
    response = characters.character_post(character=dict(data))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.FIELD_MAX_LENGTH.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_create_501st_character(characters: CharactersController, fill_db_to_max_recs: Callable[..., None]) -> None:
    """
    Тест на создание 501-ой записи о персонаже.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    fill_db_to_max_recs
    assert_equal(
        ServiceDBLimits.MAX_DB_RECORDS.value,
        len(characters.characters_get().json()['result']),
        'Ожидаемое количество {first} записей не соответствует фактической {second}',
    )
    data = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=get_random_string_with_letters_digits(10),
        other_aliases=get_random_string_with_letters_digits(10),
        universe=get_random_string_with_letters_digits(10),
        weight=get_random_float(before_dot=2, after_dot=1),
    )
    response = characters.character_post(character=dict(data))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.MORE_THAN_500_ITEMS.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_update_non_exist_character(characters: CharactersController) -> None:
    """
    Тест на изменение записи о НЕсуществующем персонаже.
    Проверка корректности возращаемого статус кода и валидности представления персонажей в теле ответа.
    """
    body = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=get_random_string_with_letters_digits(10),
        other_aliases=get_random_string_with_letters_digits(10),
        universe=get_random_string_with_letters_digits(10),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_put(character=dict(body))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.NO_SUCH_NAME.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_update_exist_character_without_required_field(characters: CharactersController) -> None:
    """
    Тест на изменение записи о существующем персонаже.
    Проверка корректности возращаемого статус кода и валидности представления персонажей в теле ответа.
    """
    body = create_new_character_data_without_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        other_aliases=get_random_string_with_letters_digits(10),
        universe=get_random_string_with_letters_digits(10),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_put(character=dict(body))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.MISSING_REQUIRED_FIELD.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_update_character_with_wrong_field_data_type(characters: CharactersController) -> None:
    """
    Тест на обновление записи о персонаже, поля в теле запроса имеют неверный тп данных.
    Проверка корректности возращаемого статус кода и сообщения об ошибке
    """
    data = create_new_character_data_with_wrong_data_type(
        education=get_random_int(10),
        height=get_random_float(),
        identity=get_random_int(10),
        name=get_random_string_with_letters_digits(10),
        other_aliases=get_random_int(10),
        universe=get_random_int(10),
        weight=get_random_float(),
    )
    response = characters.character_put(character=dict(data))
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.NOT_A_VALID_STRING.value,
        response.text,
        'Фактическое описание описание ошибки {second} не содержит ожидаемую информацию {first}'
    )


def test_delete_non_exist_character(characters: CharactersController, character_name: str) -> None:
    """
    Тест на удаление записи о существующем персонаже.
    Проверка корректности возращаемого статус кода и сообщения об ошибке.
    """
    name = get_random_string_with_letters_digits(5)
    response = characters.character_delete(name=name)
    assert_equal(
        400,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        ErrorMessages.NO_SUCH_NAME.value,
        response.text,
        'Тело ответа не соответствует ожидаемому. Ожидается {first}, фактически {second}',
    )
