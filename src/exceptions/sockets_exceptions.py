from enum import Enum
class SocketsExceptions(Enum):
    CONNECTION_REFUSED = (111, "Connection refused: The server is not accepting connections.")
    NO_ROUTE_TO_HOST = (113, "No route to host: The network is unreachable or the host is down.") 
    CONNECTION_TIMED_OUT = (110, "Connection timed out: The server did not respond in time.")
    NAME_OR_SERVICE_NOT_KNOWN = (-2, "Name or service not known: The hostname could not be resolved.") 
    UNKNOWN_HOST = (1, "Unknown host: The specified host could not be found.")
    SOCKET_TIMEOUT = (10060, "Socket timeout: The socket operation timed out.")
    ADDRESS_ALREADY_IN_USE = (98, "Address already in use: The socket address is already in use.")
    NETWORK_UNREACHABLE = (101, "Network unreachable: The network is not reachable from this host.")
    CONNECTION_RESET = (104, "Connection reset by peer: The connection was reset by the remote host.")
    HOST_UNREACHABLE = (112, "Host unreachable: The destination host is unreachable.") 
    NETWORK_DOWN = (100, "Network is down: The local network interface is not functioning.")

    def __init__(self, code, description): 
        self.code = code 
        self.description = description
 
    def __str__(self): return f"[{self.code}] {self.description}"
