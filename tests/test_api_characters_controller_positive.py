import pytest
from asserts import assert_equal, assert_in, assert_true

from characters_controller.characters import CharactersController
from characters_controller.dataclass import Character
from characters_controller.enums import ServiceDBLimits
from utilities.utils import (
    create_new_character_data_with_required_field,
    get_random_float,
    get_random_string_with_letters_digits,
    validate_characters_list_data,
)


def test_get_characters(characters: CharactersController) -> None:
    """
    Получение списка персонажей. Пользователь авторизован.
    Проверка корректности возращаемого статус кода и
     валидности представления персонажей в теле ответа
    """
    response = characters.characters_get()
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    data_validation_result = validate_characters_list_data(
        data=response.json()['result'],
    )
    assert_equal(
        'Success',
        data_validation_result,
        f'Не пройдена валидация данных персонажей. '
        f'Сообщение об ошибке - {data_validation_result}',
    )


def test_get_exist_character_by_name(
        characters: CharactersController,
        character_name: str,
) -> None:
    """
    Получение данных по конкретному персонажу. Пользователь авторизован.
    Проверка корректности возращаемого статус кода и валидности представления
    персонажей в теле ответа.
    """
    name = character_name
    response = characters.character_get(name=name)
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_true(
        Character(**response.json()['result']),
        'Не пройдена валидация данных о персонаже,'
    )


@pytest.mark.parametrize(
    'string_symbols_count',
    (10, ServiceDBLimits.STRING_FIELD_DATA_LIMIT.value),
    ids=('regular', 'max'),
)
def test_create_new_character(
        characters: CharactersController,
        string_symbols_count: int,
) -> None:
    """
    Добавление персонажа, которого имя которого еще нет на сервере.
    Пользователь авторизован.
    Ппроверка корректности возращаемого статус кода и валидности
    представления персонажей в теле ответа.
    """
    body = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(string_symbols_count),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(string_symbols_count),
        name=get_random_string_with_letters_digits(string_symbols_count),
        other_aliases=get_random_string_with_letters_digits(
            string_symbols_count,
        ),
        universe=get_random_string_with_letters_digits(string_symbols_count),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_post(character=dict(body))
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_equal(
        body,
        Character(**response.json()['result']),
        'Тело ответа не соответствует ожидаемому. '
        'Ожидается {first}, фактически {second}',
    )


def test_update_exist_character(
        characters: CharactersController,
        character_name: str,
) -> None:
    """
    Внесение изменений в данные о персонаже. Персонаж существует.
    Тело запроса корректно. Пользователь авторизован.
    Проверка корректности возращаемого статус кода и
    валидности представления персонажей в теле ответа.
    """
    body = create_new_character_data_with_required_field(
        education=get_random_string_with_letters_digits(10),
        height=get_random_float(),
        identity=get_random_string_with_letters_digits(10),
        name=character_name,
        other_aliases=get_random_string_with_letters_digits(10),
        universe=get_random_string_with_letters_digits(10),
        weight=get_random_float(before_dot=2, after_dot=1)
    )
    response = characters.character_put(character=dict(body))
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_equal(
        body,
        Character(**response.json()['result']),
        'Тело ответа не соответствует ожидаемому. '
        'Ожидается {first}, фактически {second}',
    )


def test_delete_exist_character(
        characters: CharactersController,
        character_name: str,
) -> None:
    """
    Удаление существующего персонажа. Пользователь авторизован.
    Проверка корректности возращаемого статус кода и информации о
    результате удаления персонажа.
    """
    name = character_name
    response = characters.character_delete(name=name)
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_in(
        f'Hero {name} is deleted',
        response.text,
        'Тело ответа не соответствует ожидаемому. '
        'Ожидается {first}, фактически {second}',
    )


def test_reset_characters_collection(characters: CharactersController) -> None:
    """
    Сброс коллекции в первоначальное состояние. Пользователь авторизован.
    Проверка корректности возращаемого статус кода и что количество записей
    в БД равно дефолтному.
    """
    response = characters.reset_post()
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    assert_equal(
        ServiceDBLimits.DEFAULT_DB_RECORD.value,
        len(characters.characters_get().json()['result'])
    )
