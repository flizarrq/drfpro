from enum import Enum


class Regex(Enum):
    BRAND = (
        r'^[a-zA-Z]{2,20}$',
        'only alpha 2-20 characters allowed'
    )
    NAME = (
        r'^[A-Z][a-zA-Z]{2,20}$',
        'only alpha first Uppercase 2-20 ch allowed'
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
