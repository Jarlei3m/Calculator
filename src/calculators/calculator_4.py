
from typing import Dict, List
from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator4:
  def __init__(self, driver_hanlder: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_hanlder

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    calculated_number = self.__process_data(input_data)
    
    formatted_response = self.__format_response(calculated_number)

    return formatted_response
  
  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntity("Invalid body format")
    
    input_data = body["numbers"]
    return input_data
  
  def __process_data(self, numbers: List[float]) -> float:
    result = self.__driver_handler.arithmetic_mean(numbers)

    return result
  
  def __format_response(self, calculated_number: float) -> Dict:
    return {
      "data": {
        "Calculator": 4,
        "result": round(calculated_number, 2)
      }
    }