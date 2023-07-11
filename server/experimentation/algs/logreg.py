from autoload import load_config
from algorithm import Algorithm
from sklearn.linear_model import LogisticRegression


@load_config()
class LogReg(LogisticRegression, Algorithm):
    ALGORITHM_NAME = 'Logistic Regression'
    DESCRIPTION = "Логистическая регрессия — метод построения линейного классификатора," \
                  " позволяющий оценивать апостериорные вероятности принадлежности объектов классам."

    PRE_REQ = [Algorithm.PreReq.NOT_NULL,
               Algorithm.PreReq.NUM,
               Algorithm.PreReq.NORM]

    INPUT_TYPES = [Algorithm.InputTypes.INT,
                   Algorithm.InputTypes.FLOAT,
                   Algorithm.InputTypes.BOOL]
    PARAMS = [
        {
            'name': 'C',
            'type': 'float',
            'min': '0',
            'max': '10',
            'decs': 'Параметр регуляризации'
        },
        {
            'name': 'penalty',
            'type': 'set',
            'values': ['l1', 'l2', 'elasticnet'],
            'decs': 'Штраф: функция подсчёта ошибки'
        }
    ]

    def __init__(self, C=1, penalty='l2'):
        LogisticRegression.__init__(self, penalty=penalty,
                                    C=C,
                                    random_state=0
                                    )
