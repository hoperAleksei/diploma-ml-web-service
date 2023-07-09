from abc import ABC
from enum import Enum
import pandas as pd


class Algorithm(ABC):
    class PreReq(Enum):
        NOT_NULL = 'not null'  # op
        NUM = 'num'  # ec
        NORM = 'norm'  # nd

    class InputTypes(Enum):
        INT = 'int64'
        FLOAT = 'float64'
        STRING = 'object'
        BOOL = 'bool'

    ALGORITHM_NAME = None
    """
        Название алгоритма
    """
    DESCRIPTION = None
    """
        Описание алгоритма
    """

    PRE_REQ: list[PreReq] = None
    """
        Требования к предобработки 
    """
    INPUT_TYPES: list[InputTypes] = None
    """
        Типы, которые принимает алгоритм  
    """
    PARAMS: dict = None
    """
    Параметры алгоритма 
    {
      'name_1': {
                  # 'index': 0,                       # положение в списке при передаче в функцию 
                  'type': 'int',                      # тип параметра (int, float, set) 
                  'name': 'example_int',              # имя параметра 
                  'min': 1,                           # минимальное значение параметра 
                  'max': 10                           # максимальное значение параметра
                  'decs': 'описание фичи'
                }, 
      'name_2': { 
                  # 'index': 1,                          
                  'type': 'set',
                  'name': 'example_set',
                  'values': {'uniform', 'distance'},   # все значения множества,
                  'decs': 'описание фичи'
                },
      'name_3': {
                  # 'index': 2,
                  'type': 'float',
                  'name': 'example_float',
                  'min': -1.0,
                  'max': 1.0,
                  'decs': 'описание фичи' 
                }  
    }
    """

    @staticmethod
    def get_alg_requirements(cls):

        return {
            'alg_name': cls.ALGORITHM_NAME,
            'requirements': {
                'NOT_NULL': Algorithm.PreReq.NOT_NULL in cls.PRE_REQ,
                'NUM': Algorithm.PreReq.NUM in cls.PRE_REQ,
                'NORM': Algorithm.PreReq.NORM in cls.PRE_REQ
            }
        }

    # @staticmethod
    # def get_params(cls):
    #     return cls.PARAMS

    # "params": [
    #                 {
    #                     "name": "k",
    #                     "type": "set",
    #                     "decs": "meen 123",
    #                     "values": ["123", "121"]
    #                 },
    #                 {
    #                     "name": "k",
    #                     "type": "int",
    #                     "decs": "meen 123",
    #                     "min": 1,
    #                     "max": 10
    #                 }
    #             ]

    # a = [
    #     {
    #         'alg_name': 'knn',
    #         'requirements': {
    #             'NOT_NULL': True,
    #             'NUM': False,
    #             'NORM': True
    #         }
    #     },
    #     {
    #         'alg_name': 'tree',
    #         'requirements': {
    #             'NOT_NULL': True,
    #             'NUM': False,
    #             'NORM': True
    #         }
    #     }
    # ]

    @staticmethod
    def get_input_types(input_list: list) -> list:
        output_list = list()
        for i in input_list:
            output_list.append(i.value)
        return output_list

    def check_input_types(self, x: pd.DataFrame) -> bool:  # возможно переделать под list
        """
        Функция проверки типов в X на соответствие типам, которые принимает алгоритм
        """
        list_of_types = [str(str_type) for str_type in x.dtypes]
        for i in list_of_types:
            if i not in self.get_input_types(self.INPUT_TYPES):
                return False
        return True

    @staticmethod
    def get_params_name(prarams):
        return list(prarams.keys())
