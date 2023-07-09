from server.experimentation.algorithm import Algorithm, InputTypes
from sklearn.neighbors import KNeighborsClassifier
from pydantic import BaseModel


# class Params(BaseModel):

class KNN(Algorithm):
    # ALGORITHM_NAME = 'k ближайших соседей'
    # REQ_PRE_TYPES = []
    # INPUT_TYPES = ['INT', 'FLOAT', 'DOUBLE']
    # PARAMS = [
    #     {
    #         'index': 0,
    #         'type': 'int',
    #         'name': 'n_neighbors',
    #         'min': '1',
    #         'max': 'max_object_count'
    #     },
    #     {
    #         'index': 1,
    #         'type': 'set',
    #         'name': 'weights',
    #         'values': {'uniform', 'distance'}
    #     }
    # ]

    def __init__(self, params: list):
        # """
        # Параметры:
        # n_neighbors - int
        # weights - {'uniform', 'distance'}
        # """
        self.__classifier = KNeighborsClassifier(n_neighbors=params[0], weights=params[1])
        # try:
            # self.__classifier = KNeighborsClassifier(n_neighbors=params[0],
            #                                          weights=params[1])
        # super().__init__(params)
        # self.__classifier = KNeighborsClassifier(n_neighbors=params[0], weights=params[1])
        # except Exception as e:
        #     print('ERROR')
        #     print(e)

    def fit(self, x, y):
        # TODO допилить фит и проверку типов
        try:
            self.check_input_types(x)
            self.__classifier.fit(x, y)
        except Exception as e:
            print(e)

    def predict(self, x):
        try:
            return self.__classifier.predict(x)
        except Exception as e:
            print(e)

    def _score(self, y_pred, y_true):
        pass



a = KNN([3, 'uniform'])
print('aboba')
