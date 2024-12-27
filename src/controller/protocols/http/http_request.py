from constants.http_protocol import HttpProtocol;
from constants.http_header import HttpHeader;

class Request:
    url: str
    protocol: HttpProtocol | str
    header: dict[HttpHeader | str, str | int]

    def get_params() -> list[str]:
        pass

    def get_queries() -> dict[str, str]:
        pass

    def get_fragment() -> str:
        pass

    def get_body(body: str):
        pass


# https://algumacoisa.com/outracoisa/jorel?nome=ou#0932093203
