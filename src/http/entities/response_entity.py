from http.entities.headers_entity_read_only import HeadersEntityReadOnly
from ..constants.http_protocol import HttpProtocol
from ..constants.http_status import HttpStatus
class ResponseEntity:
    __protocol: HttpProtocol
    __status: HttpStatus
    __headers: HeadersEntityReadOnly
    __body: str

    def set_body(self, body: str):
        self.__body = body

    def append_body(self, body:str):
        self.__body += body
    def get_body(self):
        return self.__body
    def encode(self):
        return self.__str__().encode("UTF-8")
    
    def __str__(self):
        return (
            f"{self.__protocol.value} {self.__status.value} {self.__status.name}"
            f"{self.__headers.serialize()}\r\n"
            f"{self.__body}"
        )
    def __init__(self, status: HttpStatus, body: str,protocol = HttpProtocol.HTTP11, headers = HeadersEntityReadOnly()):
        self.__protocol = HttpProtocol.HTTP11
        self.__headers = headers
        self.__body = body
        self.__status = status
    

