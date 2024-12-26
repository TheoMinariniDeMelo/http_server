from http_request import Request
from http_response import Response

class HttpServer: 
    addr: str
    port: int

    def __init__(self, addr: str, port: int):
        self.addr = addr
        self.port = port
        
    def listen() -> None:
        pass