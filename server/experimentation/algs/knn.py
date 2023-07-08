from autoload import load_config
from algorithm import Algorithm
from sklearn.neighbors import KNeighborsClassifier

@load_config()
class KNN(KNeighborsClassifier, Algorithm):
    ALGORITHM_NAME = 'knn'
    PRE_REQ = [Algorithm.PreReq.INT,
               Algorithm.PreReq.NOT_NULL],
    INPUT_TYPES = [Algorithm.InputTypes.INT,
                   Algorithm.InputTypes.FLOAT,
                   Algorithm.InputTypes.BOOL],
    PARAMS = {
        'n_neighbors': {
            'type': 'int',
            'min': '1',
            'max': '100'
        },
        'weights': {
            'type': 'set',
            'values': {'uniform', 'distance'}
        }
    }

    def __init__(self, n_neighbors, weights):
        KNeighborsClassifier.__init__(self, n_neighbors=n_neighbors,
                                      weights=weights
                                      )
        # print('ALG TEST FILE INIT')





