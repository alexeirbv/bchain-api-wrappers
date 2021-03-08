from enum import Enum

from enum import unique

HTTP_TIMEOUT_S = 10


@unique
class AdapterError(Enum):
    INSTANCE_REPORT_ERROR = 1
    HTTP_ERROR = 2
    INSTANCE_ZERO_HEIGHT = 3
    NO_PEERS = 4
    RESPONSE_PARSE_ERROR = 5


@unique
class ResponseType(Enum):
    HEIGHT = 1
    SYNCED = 2


COIN_FAMILIES: dict = {
    "ALGO": "Algorand",
}
