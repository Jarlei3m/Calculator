from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator3:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    
    variance_result = self.__calculate_variance(input_data)
    multiplication_result = self.__calculate_multiplication(input_data)

    self.__verify_results(variance_result, multiplication_result)

    formated_response = self.__format_response(variance_result)

    return formated_response
   

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntity("Invalid body format")
    
    input_data = body["numbers"]
    return input_data

  def __calculate_variance(self, numbers: List[float]) -> float:
    variance = self.__driver_handler.variance(numbers)
    return variance
  
  def __calculate_multiplication(self, numbers: List[float]) -> float:
    multiplication = 1
    for num in numbers:
      multiplication *= num
    
    return multiplication
  
  def __verify_results(self, variance_result: float, multiplication_result: float) -> None:
    if variance_result < multiplication_result:
      raise HttpBadRequest('Process failed: Variance lesser then multiplication')
    
  def __format_response(self, variance: float) -> Dict:
    return {
      "data": {
        "Calculator": 3,
        "variance": variance,
        "success": True
      }
    }