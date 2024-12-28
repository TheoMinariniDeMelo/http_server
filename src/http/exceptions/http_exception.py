from constants.Color import Color
from exceptions.sockets_exceptions import SocketsExceptions

class HttpException(Exception):
    def __init__(self, socket_error: SocketsExceptions, message):
        super().__init__(
            f"{socket_error.value[1]}\r\n{Color.RED_BACKGROUND}{message}{Color.RESET}" 
        )
