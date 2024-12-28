from ..constants.http_protocol import HttpProtocol
from ..constants.http_method import HttpMethod
from .headers_entity import HeadersEntity
from http.constants.http_header import HttpHeader
from ..utils.urls import Url
class RequestEntity:
    __protocol: HttpProtocol
    __url: Url
    __port: int
    __method: HttpMethod
    __headers: HeadersEntity
    __body: str

    def set_body(self, body: str):
        self.__body = body
        self.__headers.put_headers({
            HttpHeader.CONTENT_LENGTH: len(self.__body)
        })

    def append_body(self, body:str):
        self.set_body(self.__body + body)
    
    def get_url(self) -> Url:
        return self.__url
    
    def get_port(self) -> int:    
        return self.__port
    
    def get_body(self) -> str:
        return self.__body
    
    def encode(self):
        return self.__str__().encode()

    def __str__(self):
        return (
            f"\r{self.__method.value} {self.__url.get_path()} {self.__protocol.value}\r\n"
            f"{self.__headers.serialize()}\r\n"
            f"{self.__body}"
        )
    def __init__(
        self,body: str,
        method: HttpMethod, 
        url: str, 
        port: int,
        protocol = HttpProtocol.HTTP11,
        headers = HeadersEntity()
                 ):
        self.__protocol = protocol
        self.__method = method
        self.__headers = headers
        self.__url = Url(url)
        self.set_body(body)
        self.__port = port


