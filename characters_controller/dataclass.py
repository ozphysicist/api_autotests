from typing import Any, List, Optional, Union

from pydantic import BaseModel


class Character(BaseModel):
    """
    Модель описывающая представление одного персонажа.
    В данной модели обязательным является только поле name, остальные поля - опциональны
    """
    education: Optional[str] = None
    height: Optional[Any] = None
    identity: Optional[str] = None
    name: str
    other_aliases: Optional[str] = None
    universe: Optional[str] = None
    weight: Optional[Any] = None
