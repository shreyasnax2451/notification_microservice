from enum import Enum

class GlobalEnums(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)

class Status(GlobalEnums):
    active = "active"
    inactive = "inactive"