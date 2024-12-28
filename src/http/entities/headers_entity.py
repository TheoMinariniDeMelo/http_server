from .headers_entity_read_only import HeadersEntityReadOnly
from ..constants.http_header import HttpHeader

class HeadersEntity(HeadersEntityReadOnly):
    def __init__(self):
        self._headers = {}
    def put_headers(self, dict_headers: dict[HttpHeader, str | int]) -> None:
        for key,value in dict_headers.items():
            self._headers[key] = value 
        pass
    def remove_headers(self, list_headers: list[HttpHeader]) -> None:
        for key in list_headers:
            del self._headers[key] 
