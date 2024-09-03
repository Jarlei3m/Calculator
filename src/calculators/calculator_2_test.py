from typing import Dict
from pytest import raises
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
  def __init__(self, body:Dict) -> None:
    self.json = body
  
def test_calculate():
  mock_body = {
    "numbers": [2.12, 4.62, 1.32]
  }
  mock_request = MockRequest(body=mock_body)
  
  driver = NumpyHandler()
  calculator_2 = Calculator2(driver)
  formatted_response = calculator_2.calculate(mock_request)

  assert isinstance(formatted_response, dict)
  assert formatted_response =={'data': {'Calculator': 2, 'result': 0.08}}
  