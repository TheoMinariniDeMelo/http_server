from ..src.http.constants.http_method import HttpMethod
from ..src.http.entities.request_entity import RequestEntity
from ..src.http.http_request import HttpRequest

if __name__ == "__main__":
    request = RequestEntity(body = "", method = HttpMethod.GET, port=8000, url="http://0.0.0.0")
    response = HttpRequest(request).request()
    print(response)

