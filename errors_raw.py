# 400 -> Bad Request
# 422 -> Unprocessable Entity

class HttpUnprocessableEntity(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)
    self.message = message
    self.name = 'UnprocessableEntity'
    self.status_code = 422

try:
  print("Try block")
  raise HttpUnprocessableEntity("Throw exception!")
except Exception as exception:
  print("Except error!")
  print(exception.name)
  print(exception.status_code)
  print(exception.message)