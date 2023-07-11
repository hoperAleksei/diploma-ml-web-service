from autoload import load_config
from algorithm import Algorithm
from sklearn.svm import SVC


@load_config()
class SVM(SVC, Algorithm):
    ALGORITHM_NAME = 'SVM'
    DESCRIPTION = "Метод опорных векторов (Support Vector Machine) – это алгоритм Машинного обучения," \
                  " который проецирует Наблюдения в n-мерном пространстве Признаков с целью нахождения" \
                  " гиперплоскости, разделяющей наблюдения на классы"

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
            'name': 'kernel ',
            'type': 'set',
            'values': ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'],
            'decs': 'Ядро: функция, лежащая в основе алгоритма'
        }
    ]

    def __init__(self, C=1, kernel='rbf'):
        SVC.__init__(self,  C=C,
                            kernel=kernel,
                            random_state=0
                            )
