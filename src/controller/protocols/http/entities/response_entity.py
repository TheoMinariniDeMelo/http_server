import socket
from constants.http_header import HttpHeader
from constants.http_protocol import HttpProtocol

class ResponseEntity:
    __protocol: HttpProtocol
    __headers: dict[HttpHeader, str | int]
    __body: str

    def put_headers(self, dict_headers: dict[HttpHeader, str | int]) -> None:
        for key,value in dict_headers.items():
            self.headers[key] = value 

    def remove_headers(self, list_headers: list[HttpHeader]) -> None:
        for key in list_headers:
            del self.headers[key] 

    def set_body(self, body: str):

    def encode(self) -> str:
        header = ""
        for key, value in self.headers.items():
            header += key.value % value % "\r\n"
        header += "\r\n"

        return (
            self.protocol.value \
                + "\r\n" \
                + header \
                + self.body
        )
        
    def __init__(self):
        self.protocol = HttpProtocol.HTTP11
        self.headers = {}
        self.body = ""
    
