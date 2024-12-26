from enum import Enum

class ContentType(Enum):
    # Text Types
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"
    TEXT_CSS = "text/css"
    TEXT_JAVASCRIPT = "text/javascript"
    TEXT_CSV = "text/csv"
    TEXT_XML = "text/xml"

    # Image Types
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_GIF = "image/gif"
    IMAGE_WEBP = "image/webp"
    IMAGE_SVG_XML = "image/svg+xml"
    IMAGE_X_ICON = "image/x-icon"

    # Application Types
    APPLICATION_JSON = "application/json"
    APPLICATION_XML = "application/xml"
    APPLICATION_PDF = "application/pdf"
    APPLICATION_ZIP = "application/zip"
    APPLICATION_GZIP = "application/gzip"
    APPLICATION_OCTET_STREAM = "application/octet-stream"
    APPLICATION_FORM_URLENCODED = "application/x-www-form-urlencoded"
    APPLICATION_API_JSON = "application/vnd.api+json"

    # Audio Types
    AUDIO_MPEG = "audio/mpeg"
    AUDIO_OGG = "audio/ogg"
    AUDIO_WAV = "audio/wav"

    # Video Types
    VIDEO_MP4 = "video/mp4"
    VIDEO_WEBM = "video/webm"
    VIDEO_OGG = "video/ogg"

    # Multipart Types
    MULTIPART_FORM_DATA = "multipart/form-data"
    MULTIPART_BYTERANGES = "multipart/byteranges"

    # Other Common Types
    FONT_WOFF = "font/woff"
    FONT_WOFF2 = "font/woff2"
    APPLICATION_TAR = "application/x-tar"
    APPLICATION_7Z = "application/x-7z-compressed"