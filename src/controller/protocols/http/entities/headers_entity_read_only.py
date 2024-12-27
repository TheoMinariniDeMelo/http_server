from constants.http_header import HttpHeader
from typing import Self

class HeadersEntityReadOnly:
    __headers: dict[str, str | int]
    
    def put_headers(self, dict_headers: dict[str | HttpHeader, str | int]) -> Self:
        for key,value in dict_headers.items():
            
            self.headers[key] = value

        return self
    def put_header(self, header: str, value: str | int) -> Self:
        
    def remove_headers(self, list_headers: list[str | HttpHeader]) -> None:
        for key in list_headers:
            del self.headers[key]
    
    def get_headers(self) -> dict[str, str | int]:
        return self.__headers
    def decode_from_string(self, header_str: str) -> None:
        header_list = header_str.split("\r\n")
        for line in header_list:
            key_value = line.split(": ")
    def validate_key(key: str) -> None:
        try:
            HttpHeader
