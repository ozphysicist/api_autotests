from enum import Enum


class ErrorMessages(Enum):
    """Сообщения об ошибках"""
    UNAUTHORIZED = 'You have to login with proper credentials'
    NO_SUCH_NAME = 'No such name'
    MISSING_REQUIRED_FIELD = 'Missing data for required field.'
    ALREADY_EXIST = 'is already exists'
    NOT_A_VALID_NUMBER = 'Not a valid number.'
    NOT_A_VALID_STRING = 'Not a valid string.'
    FIELD_MAX_LENGTH = 'Length must be between 1 and 350.'
    MORE_THAN_500_ITEMS = "Collection can't contain more than 500 items"


class ServiceDBLimits(Enum):
    """
    Ограничения БД (Возможно их больше, других не нашла.
    В задании информации о них нет)
    """
    STRING_FIELD_DATA_LIMIT = 350
    MAX_DB_RECORDS = 500
    DEFAULT_DB_RECORD = 302
