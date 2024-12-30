from abc import abstractmethod
from http.entities.request_entity import RequestEntity
from http.entities.response_entity import ResponseEntity

class SimpleHttpHandler:
    @abstractmethod
    def handler(self, request: RequestEntity, response: ResponseEntity) -> ResponseEntity:
        return response
