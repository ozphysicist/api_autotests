from typing import Optional

from pydantic import BaseModel


class Character(BaseModel):
    education: str
    height: int
    identity: str
    name: str
    other_aliases: str
    universe: str
    weight: float