from constants.Color import Color


class IsInvalidUrlException(Exception):
    def __init__(self, url):
        super().__init__(
            f'{Color.RED_BACKGROUND}The Url: {Color.GREEN_BACKGROUND}{url}{Color.RED_BACKGROUND} Is not valid{Color.RESET}'
        )
