import numpy as np
import pandas as pd
from algorithm import Algorithm
from algs.knn import KNN

test_df = pd.DataFrame(data={'int': [1, 2, 3, 4, 5],
                             'str': ['a', 'Bb', '', 'D', 'e'],
                             'float': [1.0, 2.2, 3.3, 4.4, 5.5],
                             'negative': [-1, -2.0, -3, -4.4, -5],
                             'bool': [True, False, True, False, True],
                             'none': [pd.NA] * 5,
                             })


def alg_test(a: Algorithm):
    try:
        df = pd.read_csv('datasets/iris.csv')
        print('df')
    except Exception as e:
        print('ошибка открытия файла')
        print(e)
        return False, str(e)

    X = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
    Y = df[['variety']]

    try:
        a.fit(X, np.ravel(Y))
        print('SUCCESS fit')
    except Exception as e:
        print(e)
        return False, str(e)

    try:
        a.predict(X)
        print('SUCCESS predict ')
    except Exception as e:
        print(e)
        return False, str(e)

    try:
        a.score(X, Y)
        print('SUCCESS score')
    except Exception as e:
        print(e)
        return False, str(e)

    print('SUCCESS TEST')
    return True, 'SUCCESS'

# TODO: затестить все параметры, все значения set + Min и Max (опасно)
# TODO: затестить допустимые параметры типов
# TODO: затестить допустимые параметры обработок

# print('START')
# knn = KNN(3, 'uniform')
# alg_test(knn)
