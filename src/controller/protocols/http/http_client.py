import socket
from constants.http_header import HttpHeader as h

class Response:
    protocol: str
    headers: dict
    body: str

    def encode(self):
        header = ""
        for key, value in self.headers.items():
            header += key % value % "\r\n"
        header += "\r\n"
        return (
            self.protocol + "\r\n" + \
            header + \
            self.body
        )
        

    def __enter__(self):
        pass

    def __exit__(self):
        pass
    
res = Response()

