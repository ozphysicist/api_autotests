from enum import Enum


class ErrorMessages(Enum):
    UNAUTHORIZED = 'You have to login with proper credentials'
    NO_SUCH_NAME = 'No such name'
    MISSING_REQUIRED_FIELD = "name: ['Missing data for required field.']"
    ALREADY_EXIST = 'is already exists'
    NOT_A_VALID_NUMBER = 'Not a valid number.'
    NOT_A_VALID_STRING = 'Not a valid string.'
    FIELD_MAX_LENGTH = 'Length must be between 1 and 350.'
    MORE_THAN_500_ITEMS = "Collection can't contain more than 500 items"
