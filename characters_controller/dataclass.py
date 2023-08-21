from typing import Any, Optional

from pydantic import BaseModel


class Character(BaseModel):
    """
    Модель описывающая представление одного персонажа.
    В данной модели обязательным является только поле name,
    остальные поля - опциональны.
    """
    education: Optional[str] = None
    height: Optional[Any] = None
    identity: Optional[str] = None
    name: str
    other_aliases: Optional[str] = None
    universe: Optional[str] = None
    weight: Optional[Any] = None


class CharacterWithoutName(BaseModel):
    """
    Модель описывающая представление одного персонажа,
    в которой отсутствует обязательное поле name.
    Остальные поля - опциональны.
    """
    education: Optional[str] = None
    height: Optional[Any] = None
    identity: Optional[str] = None
    other_aliases: Optional[str] = None
    universe: Optional[str] = None
    weight: Optional[Any] = None


class CharacterWrongTypeModel(BaseModel):
    """
    Модель описывающая представление одного персонажа,
    типы данных неверны.
    """
    education: Optional[int] = None
    height: Optional[float] = None
    identity: Optional[int] = None
    name: str
    other_aliases: Optional[int] = None
    universe: Optional[int] = None
    weight: Optional[float] = None
