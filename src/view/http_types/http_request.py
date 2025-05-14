class HttpRequest:
  def __init__(self, body: dict = None, param=None)-> None:
    self.body = body
    self.param= param

    