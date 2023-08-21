import decimal
import random
import string
from typing import Any, Optional

from pydantic import ValidationError

from characters_controller.characters import CharactersController
from characters_controller.dataclass import (
    Character,
    CharacterWithoutName,
    CharacterWrongTypeModel,
)


def validate_characters_list_data(data: Any) -> str:
    """Метод валидации полученных данных о персонажах со схемой"""
    try:
        for record in data:
            Character(**record)
    except ValidationError as error_message:
        return error_message
    else:
        return 'Success'


def get_exist_random_character_name(
        controller: CharactersController,
        type_name: Optional[str] = None,
) -> str:
    """
    Метод, возвращающий случайное имя существующего героя.
    Исходим из того, что в таблице БД сервиса всегда есть записи о персонажах.
    Если бы таблица была пустой, то мы бы сначала добавляли персонажа,
    потом искали запись о не в БД, а после удаляли эту запись
    (в этом случае было бы реализовано с использованием фикстуры).
    """
    characters_list = controller.characters_get().json()['result']
    random.shuffle(characters_list)
    name = random.choice(characters_list)['name']
    if type_name == 'with_space':
        return name
    else:
        return name.replace(' ', '+') if '' in name else name


def get_random_string_with_letters_digits(length: int) -> str:
    """
    Метод, возвращающий cлучайное строковое значение из букв а
    нглийского алфавита (верхний и нижний регистр) и цифр
    :param: length: длина строки
    :return: строка заданной длины
    """
    result = random.choices(
        string.ascii_lowercase + string.ascii_uppercase + string.digits,
        k=length,
    )
    return ''.join(result)


def get_random_int(length: int) -> int:
    """Метод, возвращающий случайное целое число заданной длины"""
    result = random.choices(string.digits, k=length)
    return int(''.join(result))


def get_random_float(before_dot: int = 1, after_dot: int = 2) -> float:
    """
    Метод генерирующий случайное вещественное число.
    :param before_dot: количество символов целочисленной части.
    :param after_dot: количество символо длина дробной части.
    """
    left_part = random.choices(string.digits, k=before_dot)
    left_part = ''.join(left_part)
    # Обрабатываем случай когда первым символом стоит 0
    if left_part.startswith('0'):
        left_part = left_part[:0] + str(random.randint(1, 9)) + left_part[1:]
    right_part = random.choices(string.digits, k=after_dot)
    right_part = ''.join(right_part)
    # Обрабатываем случай когда последним символом стоит 0
    if right_part.endswith('0'):
        right_part = right_part[:-1] + str(random.randint(1, 9)) \
                     + right_part[-1:-1]
    return float(decimal.Decimal(left_part + '.' + right_part))


def create_new_character_data_with_required_field(
        education: str,
        height: float,
        identity: str,
        name: str,
        other_aliases: str,
        universe: str,
        weight: float,
) -> Character:
    """
    Метод, создающий объект Character со всеми обязательными полями
    и верными типами данных.
    """
    data = Character(
        education=education,
        height=height,
        identity=identity,
        name=name,
        other_aliases=other_aliases,
        universe=universe,
        weight=weight,
    )
    return data


def create_new_character_data_without_required_field(
        education: str,
        height: float,
        identity: str,
        other_aliases: str,
        universe: str,
        weight: float,
) -> CharacterWithoutName:
    """
    Метод, создающий объект Character без обязательного поля name.
    """
    data = CharacterWithoutName(
        education=education,
        height=height,
        identity=identity,
        other_aliases=other_aliases,
        universe=universe,
        weight=weight,
    )
    return data


def create_new_character_data_with_wrong_data_type(
        education: int,
        height: float,
        identity: int,
        name: str,
        other_aliases: int,
        universe: int,
        weight: float,
) -> CharacterWrongTypeModel:
    """
    Метод, создающий объект Character со всеми обязательными полями
    и НЕверными типами данных в полях education, identity, other_aliases,
    universe.
    """
    data = CharacterWrongTypeModel(
        education=education,
        height=height,
        identity=identity,
        name=name,
        other_aliases=other_aliases,
        universe=universe,
        weight=weight,
    )
    return data
