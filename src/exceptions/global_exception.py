from enum import Enum
from global_exception_type import GlobalExceptionType

class GlobalException(Enum):
    # Checker Exceptions
    INVALID_HOSTNAME = ("Invalid Hostname", "The provided hostname is not valid.", "CHECKER"),
    INVALID_PORT = ("Invalid Port", "The provided port number is not valid.", "CHECKER"),

    name: str
    message: str
    type: GlobalExceptionType

    def __init__(self, name: str, message: str, type: GlobalExceptionType):
        self.name = name
        self.message = message
        self.type = type

    def get_name(self):
        return self.name
    
    def get_message(self):
        return self.message
    
    def get_type(self):
        return self.type