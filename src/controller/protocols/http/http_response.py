import socket
from constants.http_header import HttpHeader
from constants.http_protocol import HttpProtocol

class Model:
    protocol: HttpProtocol
    headers: dict[HttpHeader, str | int]
    body: str
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
    

