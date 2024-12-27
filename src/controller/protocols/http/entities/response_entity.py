import socket
from constants.http_header import HttpHeader
from constants.http_protocol import HttpProtocol
from constants.http_status import HttpStatus
from entities.headers_entity import HeadersEntity
class ResponseEntity:
    __protocol: HttpProtocol
    __status: HttpStatus
    __headers: HeadersEntity
    __body: str

    def put_headers(self, dict_headers: dict[str, str | int]) -> None:
        for key,value in dict_headers.items():
            self.headers[key] = value 

    def remove_headers(self, list_headers: list[str]) -> None:
        for key in list_headers:
            del self.headers[key] 

    def set_body(self, body: str):
        self.body = body

    def append_body(self, body:str):
        self.body += body

    def encode(self):
        header = ""
        for key, value in self.headers.items():
            header += key.value % value % "\r\n"
        header += "\r\n"
        return (
            f"{self.protocol.value} {self.status.value} {self.status.name}"
            f"{header}\r\n"
            f"{self.body}"
        )
    def __init__(self, status: HttpStatus, body: str,protocol = HttpProtocol.HTTP11, headers = {}):
        self.protocol = HttpProtocol.HTTP11
        self.headers = headers
        self.body = body
        self.status = status


