import re
from urllib.parse import urlparse

from exceptions.url_exception import IsInvalidUrlException
class Url:
    __url: str
    
    def __init__(self, url: str):
        Url.validate_url(url)
        self.__url = url

    @staticmethod
    def validate_url(url:str): # Padrão de expressão regular para validar URLs 
        pattern = re.compile( r'^(https?|ftp)://' # Protocolo (http, https, ftp) 
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # Domínio 
            r'localhost|' # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # Endereço IP (IPv4)
            r' \[?[A-F0-9]*:[A-F0-9:]+\] ?)' # Endereço IP (IPv6)
            r'(?::\d+)?' # Porta opcional 
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        if not re.match(pattern, url):
            raise IsInvalidUrlException(url)

    def get_path(self): 
        return urlparse(self.__url).path

    def get_params(self): 
        return urlparse(self.__url).params

    def get_fragment(self): 
        return urlparse(self.__url).fragment


    def set_value(self, url: str) -> None:
        Url.validate_url(url)
        self.__url = url

    def get_value(self) -> str:
        return self.__url
    
