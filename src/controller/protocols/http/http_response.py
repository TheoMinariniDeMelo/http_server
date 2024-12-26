import socket
from constants.http_header import HttpHeader
from constants.http_protocol import HttpProtocol

class Response:
    protocol: HttpProtocol
    headers: dict[HttpHeader, str | int]
    body: str
    connection_socket: socket.socket 
    def __encode(self):
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
        

    def __enter__(self):
        self.protocol = HttpProtocol.HTTP11
        self.headers = {}
        self.body = ""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):




with Response() as reponse:
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reponse.body = "Hello world!"
    reponse.headers = {
        HttpHeader.CONTENT_LENGTH: 123
    }
    reponse.connection_socket
