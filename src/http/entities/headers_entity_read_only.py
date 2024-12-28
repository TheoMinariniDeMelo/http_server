from ..constants.http_header import HttpHeader
from typing import Self

from exceptions.http_exception import HttpException
from exceptions.sockets_exceptions import SocketsExceptions

class HeadersEntityReadOnly:
    _headers: dict[HttpHeader, str | int]

    def __init__(self, header = ""):
        self._headers = self._decode_from_string(header)

    def get_headers(self) -> dict[HttpHeader, str | int]:
        return self._headers

    def _validate_header(self, value: str) -> tuple[bool, str | None]:
        try:
            HttpHeader(value.replace(" ", ""))
        except ValueError as error:
            return (False, str(error))
        return (True, None)
    
    def serialize(self):
        return ''.join(f"{key.value}: {value}\r\n" for key, value in self.get_headers().items())
    def _decode_from_string(self, header_str: str) -> dict[HttpHeader, str | int]:
        if not len(header_str):
            return {}
        header_list = header_str.split("\r\n")
        headers = {}
        error_list = []
        for line in header_list:
            header = line.split(": ")
            b = self._validate_header(header[0])
            if not b[1] is None:
                error_list.append(b[1])
            else:
                headers[HttpHeader(header[0])] = header[1]
        if not len(error_list) == 0:
            raise HttpException(SocketsExceptions.APPLICATION,'Header Error:\r\n'.join(error_list))
        return headers
