import os
import socket
from http.constants.http_method import HttpMethod
from http.constants.http_protocol import HttpProtocol
from http.constants.http_status import HttpStatus
from http.entities.headers_entity import HeadersEntity
from http.entities.headers_entity_read_only import HeadersEntityReadOnly
from http.entities.request_entity import RequestEntity
from http.entities.response_entity import ResponseEntity
from http.utils.urls import Url
from simple_http_handler import SimpleHttpHandler

class HttpServer: 
    __addr: tuple[str, int]
    __socket: socket.socket
    __handler: SimpleHttpHandler

    def __init__(self, addr: tuple[str, int], handler: SimpleHttpHandler):
        self.__addr = addr
        self.__handler = handler
    def start(self) -> None:
        if(self.__addr[1] > 65535 or self.__addr[1] <= 0):
            pass
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        domain = Url(self.__addr[0]).get_domain()
        port = self.__addr[1]
        self.__socket.connect((domain, port))
        self.__socket.listen(10)
        os.fork()
        while True:
            s_client, _ = self.__socket.accept()
            request_b = self.__recv_data(s_client)
            request = self.__process_request(request_b, (self.__addr[0], 0))
            response = ResponseEntity(status = HttpStatus(500), body="") 
            self.__handler.handler(request, response)
            s_client.send(response.encode()) 
            s_client.close()
    def __recv_data(self, socket_connection: socket.socket, buffer_size: int = 1024) -> bytes:
        response = b''
        while True:
            data = socket_connection.recv(buffer_size)
            if not data:
                break
            response += data
        return response

    def __process_request(self, request_b: bytes, host:tuple[str, int]) -> RequestEntity:
        request_text = request_b.decode('UTF-8')

        # Extraindo partes da resposta
        first_break_line = request_text.find("\r\n")
        first_line = request_text[:first_break_line]
        method = self.__get_method(first_line)
        path = self.__get_path(first_line)
        protocol = self.__get_protocol(first_line)
        
        last_header_break_line = request_text.find("\r\n\r\n")
        headers_raw = request_text[first_break_line + 2:last_header_break_line]
        body = request_text[last_header_break_line + 4:]

        # Criando entidades
        headers = HeadersEntity()
        headers.put_headers(HeadersEntityReadOnly(headers_raw).get_headers())
        protocol = HttpProtocol(protocol)
        return RequestEntity(
            body=body,
            method = HttpMethod(method),
            url = f'{host[0]}{path}',
            port= host[1],
            protocol=protocol,
            headers=headers
        )
    def __get_method(self, line: str) -> str:
        return line.split(" ")[0]
    def __get_path(self, line: str) -> str:
        return line.split(" ")[1]
    def __get_protocol(self, line: str) -> str:
        # Obtendo o protocolo HTTP da linha
        return line.split(" ")[2]  
