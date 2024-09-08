from typing import Dict, List

from .calculator_4 import Calculator4

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler:
  def arithmetic_mean(self, numbers: List[float]) -> float:
    return 3
  
def test_calculate():
  mock_body = {
    "numbers": [1, 2, 3, 4, 5]
  }
  mock_request = MockRequest(body=mock_body)
  calculator_4 = Calculator4(MockDriverHandler())

  formatted_response = calculator_4.calculate(mock_request)

  assert isinstance(formatted_response, dict)
  assert formatted_response == {'data': {'Calculator': 4, 'result': 3}}
