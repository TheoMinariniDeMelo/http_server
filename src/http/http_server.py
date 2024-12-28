import socket
import asyncio
from http_request import HttpRequest
#from http_response import Response

class HttpServer: 
    __addr: str
    __port: int
    __socket: socket.socket
    def __init__(self, addr_port: tuple[str, int]):
        self.__addr = addr_port[0]
        self.__port = addr_port[1]
         
    def start(self) -> None:
        if(self.__port > 65535 or self.__port <= 0):
            #raise
            pass
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.listen(10)
        while True:
            pass

