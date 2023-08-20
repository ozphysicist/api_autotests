from typing import List

from characters_controller.characters import CharactersController
from characters_controller.enums import ErrorMessages
from utilities.utils import validate_characters_list_data

from asserts import assert_equal


def test_get_characters_response_status_is_ok(characters: CharactersController) -> None:
    """
    Тест на получение списка персонажей:
    проверка корректности возращаемого статус кода и валидности представления персонажей в теле ответа
    """
    response = characters.characters_get()
    assert_equal(
        200,
        response.status_code,
        'Некорректный код ответа. Ожидается {first}, фактически {second}',
    )
    data_validation_result = validate_characters_list_data(data=response.json()['result'])
    assert_equal(
        'Success',
        data_validation_result,
        f'Не пройдена валидация данных персонажей. Сообщение об ошибке - {data_validation_result}',
    )




