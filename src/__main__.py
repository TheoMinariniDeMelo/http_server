import sys

sys.path.append("./http")
from http.entities.request_entity import RequestEntity
from http.constants.http_method import HttpMethod
from http.http_request import HttpRequest


if __name__ == "__main__":
    request = RequestEntity(body = "", method = HttpMethod.GET, port=8000, url="http://localhost:8000/docker-compose.yaml")
    response = HttpRequest(request).request()
    print(response.get_body())

