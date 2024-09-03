from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_body = {
    "number": 1
  }
  mock_request = MockRequest(body=mock_body)
  
  calculator_1 = Calculator1()
  response = calculator_1.calculate(mock_request)

  # Response format
  assert "data" in response
  assert "Calculator" in response["data"]
  assert "result" in response["data"]

  # Response assert
  assert response["data"]["Calculator"] == 1
  assert response["data"]["result"] == 14.25

def test_calculate_with_body_error():
  mock_body = {
    "something": 1
  }
  mock_request = MockRequest(body=mock_body)
  calculator_1 = Calculator1()

  with raises(Exception) as excinfo:
    calculator_1.calculate(mock_request)

  assert str(excinfo.value) == "Invalid body format"