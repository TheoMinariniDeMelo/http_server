from constants.http_protocol import HttpProtocol;
from constants.http_header import HttpHeader;

class Request:
    url: str
    protocol: HttpProtocol | str
    header: dict[HttpHeader | str, str | int]

    def get_path_params() -> list[str]:
        pass

    def get_queries_params() -> dict[str, str]:
        pass

    def get_body(body: str):
        pass