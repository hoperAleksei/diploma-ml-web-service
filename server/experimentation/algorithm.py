from abc import ABC, abstractmethod
from enum import Enum
from pydantic import BaseModel
import pandas as pd


class PreTypes(Enum):
    NOT_NULL = 'not null'

class InputTypes(Enum):
    INT = 'int64'
    FLOAT = 'float64'
    STRING = 'object'
    BOOL = 'bool'

class AlgorithmParam(BaseModel):
    ALGORITHM_NAME = ''
    """
        Название алгоритма
    """
    REQ_PRE_TYPES: list[PreTypes]
    """
        Требования к предобработки 
    """
    INPUT_TYPES: list[InputTypes]
    """
        Типы, которые принимает алгоритм  
    """
    PARAMS: list[dict]
    """
    Параметры алгоритма 
    [
      {
        'index': 0                          # положение в списке при передаче в функцию 
        'type': 'int',                      # тип параметра (int, float, set) 
        'name': 'example_int',              # имя параметра 
        'min': 1,                           # минимальное значение параметра 
        'max': 10                           # максимальное значение параметра | кол-во объектов - 'max_object_count'
      }, 
      { 
        'index': 1                          
        'type': 'set',
        'name': 'example_set',
        'values': {'uniform', 'distance'}   # все значения множества
      },
      {
        'index': 2 
        'type': 'float',
        'name': 'example_float',
        'min': -1.0,
        'max': 1.0 
      }  
    ]
    """


class Algorithm(ABC, AlgorithmParam):
# class Algorithm(ABC):
    @abstractmethod
    def __init__(self, params: list) -> None:
        """
            Функция инициализации гиперпараметров.
            Входные параметры: гиперпарамметры алгоритма.
        """
        pass


    @staticmethod
    def get_input_types(input_list: list[InputTypes]) -> list[str]:
        output_list = list()
        for i in input_list:
            output_list.append(InputTypes[i].value)
        return output_list


    def check_input_types(self, x: pd.DataFrame) -> bool: # возможно переделать под list
        """
        Функция проверки типов в X на соответствие типам, которые принимает алгоритм
        """
        list_of_types = [str(str_type) for str_type in x.dtypes]
        for i in list_of_types:
            if i not in self.get_input_types(self.INPUT_TYPES):
                return False
        return True


    @abstractmethod
    def fit(self, x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
        """
            Функция обучения алгоритма
        """
        pass


    @abstractmethod
    def predict(self, x):
        """
            Функция предсказания значения
        """
        pass



    @abstractmethod
    def _score(self, y_pred, y_true):
        """
            Функция получения confusion matrix
        """
        pass

