from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_hanlder_interface import DriverHandlerInterface

class MockRequest:
  def __init__(self, body:Dict) -> None:
    self.json = body

class MockDriverHandler:
  def standard_deviation(self, numbers: List[float]) -> float:
    return 3
  
# NumpyHandler and Calculator2 integration
def test_calculate_integration():
  mock_body = {
    "numbers": [2.12, 4.62, 1.32]
  }
  mock_request = MockRequest(body=mock_body)
  
  driver = NumpyHandler()
  calculator_2 = Calculator2(driver)
  formatted_response = calculator_2.calculate(mock_request)

  assert isinstance(formatted_response, dict)
  assert formatted_response =={'data': {'Calculator': 2, 'result': 0.08}}
  
def test_calculate():
  mock_body = {
    "numbers": [2.12, 4.62, 1.32]
  }
  mock_request = MockRequest(body=mock_body)
  
  driver = MockDriverHandler()
  calculator_2 = Calculator2(driver)
  formatted_response = calculator_2.calculate(mock_request)

  assert isinstance(formatted_response, dict)
  assert formatted_response =={'data': {'Calculator': 2, 'result': 0.33}}
  