from exceptions.sockets_exceptions import SocketsExceptions

class HttpException(Exception):
    def __init__(self, socket_error: SocketsExceptions):
        super().__init__(socket_error.value)
