from enum import Enum

class HttpProtocol(Enum):
    HTTP10 = 'HTTP/1.0'
    HTTP11 = 'HTTP/1.1'
    HTTP2 = 'HTTP/2'
    HTTP3 = 'HTTP/3'