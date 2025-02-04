from enum import Enum

class HttpHeader(Enum):
    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    ACCEPT_RANGES = "Accept-Ranges"
    ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
    AGE = "Age"
    ALLOW = "Allow"
    AUTHORIZATION = "Authorization"
    CACHE_CONTROL = "Cache-Control"
    CONNECTION = "Connection"
    CONTENT_ENCODING = "Content-Encoding"
    CONTENT_LANGUAGE = "Content-Language"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_LOCATION = "Content-Location"
    CONTENT_MD5 = "Content-MD5"
    CONTENT_RANGE = "Content-Range"
    CONTENT_TYPE = "Content-Type"
    COOKIE = "Cookie"
    DATE = "Date"
    ETAG = "ETag"
    EXPECT = "Expect"
    EXPIRES = "Expires"
    FROM = "From"
    HOST = "Host"
    IF_MATCH = "If-Match"
    IF_MODIFIED_SINCE = "If-Modified-Since"
    IF_NONE_MATCH = "If-None-Match"
    IF_RANGE = "If-Range"
    IF_UNMODIFIED_SINCE = "If-Unmodified-Since"
    LAST_MODIFIED = "Last-Modified"
    LOCATION = "Location"
    MAX_FORWARDS = "Max-Forwards"
    PRAGMA = "Pragma"
    PROXY_AUTHENTICATE = "Proxy-Authenticate"
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    RANGE = "Range"
    REFERER = "Referer"
    RETRY_AFTER = "Retry-After"
    SERVER = "Server"
    SET_COOKIE = "Set-Cookie"
    TE = "TE"
    TRAILER = "Trailer"
    TRANSFER_ENCODING = "Transfer-Encoding"
    UPGRADE = "Upgrade"
    USER_AGENT = "User-Agent"
    VARY = "Vary"
    VIA = "Via"
    WARNING = "Warning"
    WWW_AUTHENTICATE = "WWW-Authenticate"
    
    def __new__(cls, value: str): # Normalizar o valor para aceitar tanto maiúsculas quanto minúsculas
        obj = object.__new__(cls) 
        obj._value_ = value.lower() 
        return obj
    
    @classmethod 
    def _missing_(cls, value): # Verificar se o valor está no enum, independentemente de maiúsculas/minúsculas
        for member in cls: 
            if member.value == value.lower(): 
                return member 
        raise ValueError(f"{value} is not a valid {cls.__name__}")    
# Função para imprimir o nome de um cabeçalho HTTP
def print_http_header_name(header):
    print(header.value)

