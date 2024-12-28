from enum import Enum

class Color(Enum):
    RESET = "\u001B[0m"
    RED_BACKGROUND = "\u001B[48;5;52m"
    GREEN_BACKGROUND = "\u001B[42m"
    WHITE = "\u001B[97m"
