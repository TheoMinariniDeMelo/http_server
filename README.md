# Http Client

- Header
  method: Method | str = None
  host: str = None
  Content-Type: ContentType | str = None
  Authorization: str = None
  Content-Lenght: int = None

  __init__()

  def get_method()
  def set_method(Method)

- Response
  setHeader(header: Header)

  send(response)
  close()

  __init__()

- Request
  header: Header
  body: str

  __init__()