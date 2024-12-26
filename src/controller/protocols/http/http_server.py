import socket
import asyncio
from http_request import Request
from http_response import Response

class HttpServer: 
    __addr: str
    __port: int
    __socket: socket.socket
    def __init__(self, addr: str, port: int):
        self.addr = addr
        self.port = port
         
    def start(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.listen(10)
        while True:


