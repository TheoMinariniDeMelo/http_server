from global_exception import GlobalException
from global_exception_type import GlobalExceptionType
from constants.Color import Color

class GlobalExceptionHandler: 
    def __init__(exception: GlobalException):
        print(Color.RED_BACKGROUND + Color.WHITE + " " + exception.get_type() + " ERROR: " + exception.get_name() + " -> " + exception.get_message() + Color.RESET)

    def __init__(self, name: str, message: str, type: GlobalExceptionType):
        print(Color.RED_BACKGROUND + Color.WHITE + " " + type + " ERROR: " + name + " -> " + message + Color.RESET)