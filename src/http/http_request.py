import socket
import ssl
from .constants.http_protocol import HttpProtocol
from .constants.http_status import HttpStatus
from .entities.headers_entity_read_only import HeadersEntityReadOnly
from .entities.request_entity import RequestEntity
from .entities.response_entity import ResponseEntity

class HttpRequest:
    def __init__(self, request: RequestEntity):
        self.__request = request

    def request(self) -> ResponseEntity:
        # Configuração do socket
        domain = self.__request.get_url().get_domain()
        port = self.__request.get_port()
        if self.__request.get_url().is_https_url():
            return self.__request_https((domain, port))
        return self.__request_http((domain, port))

    def __request_https(self, address: tuple[str, int]):
        context = ssl.create_default_context()
        print(f"Conectando em {address}")
        with socket.create_connection(address) as sock:
            with context.wrap_socket(sock, server_hostname=address[0]) as ssock:
                response = self.__recv_data(ssock)
                sock.close()
                return self.__process_request(response)

    def __request_http(self, address: tuple[str, int]): 
        # Resolvendo host e conectando 
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Conectando em {address}")

        sc.connect(address)
        sc.send(self.__request.encode())
        # Recebendo a resposta
        response_data = self.__recv_data(sc)
        sc.close()

        # Processando a resposta
        return self.__process_request(response_data)

    def __recv_data(self, socket_connection: socket.socket, buffer_size: int = 1024) -> bytes:
        response = b''
        while True:
            data = socket_connection.recv(buffer_size)
            if not data:
                break
            response += data
        return response

    def __process_request(self, response_b: bytes) -> ResponseEntity:
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

