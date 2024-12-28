import socket
from .constants.http_protocol import HttpProtocol
from .constants.http_header import HttpHeader
from .constants.http_status import HttpStatus
from .entities.headers_entity_read_only import HeadersEntityReadOnly
from .entities.request_entity import RequestEntity
from .entities.response_entity import ResponseEntity

class HttpRequest:
    def __init__(self, request: RequestEntity):
        self.__request = request

    def request(self) -> ResponseEntity:
        # Configuração do socket
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        url = self.__request.get_url().get_value().replace("http://", "")
        port = self.__request.get_port()

        # Resolvendo host e conectando
        host = url.split(":")[0]
        print(f"Conectando em {host}, {port}")
        sc.connect((host, port))
        sc.send(self.__request.encode())
        # Recebendo a resposta
        response_data = self.__receive_data(sc)
        sc.close()

        # Processando a resposta
        return self.process_request(response_data)

    def __receive_data(self, socket_connection: socket.socket, buffer_size: int = 1024) -> bytes:
        response = b''
        while True:
            print("A")
            data = socket_connection.recv(buffer_size)
            print("B")
            if not data:
                break
            response += data
        return response

    def process_request(self, response_b: bytes) -> ResponseEntity:
        response_text = response_b.decode('UTF-8')

        # Extraindo partes da resposta
        first_break_line = response_text.find("\r\n")
        first_line = response_text[:first_break_line]
        status = self.__get_status(first_line)
        protocol = self.__get_protocol(first_line)

        last_header_break_line = response_text.find("\r\n\r\n")
        headers_raw = response_text[first_break_line + 2:last_header_break_line]
        body = response_text[last_header_break_line + 4:]

        # Criando entidades
        headers = HeadersEntityReadOnly(headers_raw)
        status = HttpStatus(status)
        protocol = HttpProtocol(protocol)
        return ResponseEntity(
            status=status,
            body=body,
            protocol=protocol,
            headers=headers
        )

    def __get_status(self, line: str) -> str:
        # Obtendo o status HTTP da linha
        return line.split(" ")[1]

    def __get_protocol(self, line: str) -> str:
        # Obtendo o protocolo HTTP da linha
        return line.split(" ")[0]

