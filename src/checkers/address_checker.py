from exceptions.global_exception import GlobalException
from exceptions.global_exception_handler import GlobalExceptionHandler

class AddressChecker:
    def checkAll(self, hostname: str, port: int):
        self.checkHostname(hostname)
        self.checkPort(port)
        pass

    def checkHostname(self, hostname: str):
        if hostname == "":
            raise GlobalExceptionHandler(GlobalException.INVALID_HOSTNAME)
        pass

    def checkPort(self, port: int):
        if port < 0 or port > 65535:
            raise GlobalExceptionHandler(GlobalException.INVALID_PORT)
        pass