from constants.Color import Color


class IsInvalidUrlException(Exception):
    def __init__(self, url):
        super().__init__(
            f'{Color.RESET.value}{Color.RED_BACKGROUND.value}The Url:{Color.RESET.value}{Color.GREEN_BACKGROUND.value}{url} {Color.RESET.value}{Color.RED_BACKGROUND.value}Is not valid{Color.RESET.value}'
        )
