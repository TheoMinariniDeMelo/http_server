import socket

def url_and_port_validator(url: str, port: int):
    return (1,2)

def request(url: str, port: int):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    url, port = url_and_port_validator(url, port)
    sc.connect((url, port))

