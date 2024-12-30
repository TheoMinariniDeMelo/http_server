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
        pattern = re.compile(
            r'^(https?):\/\/'                # Protocolo (http ou https)
                r'([a-zA-Z0-9.-]+)'              # Nome de domínio
                r'(\.[a-zA-Z]{2,})'              # Extensão (ex: .com, .org)
                r'(\/[^\s]*)?$'                  # Caminho opcional
        )
        if not bool(re.match(pattern, url)):    
            raise IsInvalidUrlException(url)  

    def is_https_url(self) -> bool:
        pattern = r'^https://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(:\d+)?(/[^\s]*)?$'
        return re.match(pattern, self.__url) is not None
    def get_domain(self) -> str:
           return urlparse(self.__url).netloc 
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

