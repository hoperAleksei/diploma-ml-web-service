from autoload import load_config
from sklearn.neighbors import KNeighborsClassifier
from algorithm import Algorithm


@load_config()
class KNN(KNeighborsClassifier, Algorithm):
    ALGORITHM_NAME = 'k-nearest neighbors'
    DESCRIPTION = "Метод ближайших соседей — простейший метрический классификатор, основанный на оценивании" \
                  " сходства объектов. Классифицируемый объект относится к тому классу, которому принадлежат" \
                  " ближайшие к нему объекты обучающей выборки."

    PRE_REQ = [Algorithm.PreReq.NUM,
               Algorithm.PreReq.NOT_NULL]

    INPUT_TYPES = [Algorithm.InputTypes.INT,
                   Algorithm.InputTypes.FLOAT,
                   Algorithm.InputTypes.BOOL]
    PARAMS = {
        'n_neighbors': {
            'type': 'int',
            'min': '1',
            'max': '100',
            'decs': 'Количество соседей'
        },
        'weights': {
            'type': 'set',
            'values': ['uniform', 'distance'],
            'decs': 'Способ голосования'
        }
    }

    def __init__(self, n_neighbors=3, weights='uniform'):
        KNeighborsClassifier.__init__(self, n_neighbors=n_neighbors,
                                      weights=weights
                                      )
