# Http Client

- Header
  method: Method | str = None
  host: str = None
  Content-Type: ContentType | str = None
  Authorization: str = None
  Content-Lenght: int = None

  __init__()

- Response
  setHeader(Header)

  send(response)
  close()

  __init__()

- Request
  header: Header
  body: str

  __init__()