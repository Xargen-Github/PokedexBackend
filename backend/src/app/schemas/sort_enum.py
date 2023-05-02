from enum import Enum, IntEnum

class SortEnum(str, Enum):
    NAME_ASC = 'name-asc'
    NAME_DESC = 'name-desc'
    ID_ASC = 'id-asc'
    ID_DESC = 'id-desc'