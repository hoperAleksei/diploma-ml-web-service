import numpy as np
import pandas as pd
from .algs.algorithm import Algorithm
# from algs.knn import KNN
from .loader import algs_loader, get_alg_by_file_name

from sklearn.datasets import load_iris

X_test_df = pd.DataFrame(data={'int': [1, 2, 3, 4, 5],
                               'str': ['a', 'Bb', '', 'D', 'e'],
                               'float': [1.0, 2.2, 3.3, 4.4, 5.5],
                               'negative': [-1, -2.0, -3, -4.4, -5],
                               'bool': [True, False, True, False, True],
                               'none': [pd.NA, pd.NA, pd.NA, pd.NA, 1]
                               })

Y_test_df = pd.DataFrame(data={'target': [0, 1, 2, 1, 0]})


def alg_test(a: Algorithm):
    """
    Тестирование алгоритма

    :return: (bool, str)
    """
    try:
        df = load_iris()
        print('df')

        X = df.data
        Y = df.target

    except Exception as e:
        print('ошибка открытия файла')
        print(e)
        return False, "load df exception: " + str(e)

    try:
        a.fit(X, Y)
        print('SUCCESS fit')
    except Exception as e:
        print(e)
        return False, "fit exception: " + str(e)

    try:
        a.predict(X)
        print('SUCCESS predict ')
    except Exception as e:
        print(e)
        return False, "predict exception: " + str(e)

    try:
        a.score(X, Y)
        print('SUCCESS score')
    except Exception as e:
        print(e)
        return False, "score exception: " + str(e)

    print('SUCCESS SMOKE TEST')

    print('data type test')
    try:

        if 'float64' in Algorithm.get_input_types(a.INPUT_TYPES):
            print('float test')
            a.fit(pd.DataFrame(X_test_df['float']), pd.DataFrame(Y_test_df))

        print('SUCCESS float test')
    except Exception as e:
        print(e)
        return False, "data float exception: " + str(e)

    try:
        if Algorithm.InputTypes.STRING.value in Algorithm.get_input_types(a.INPUT_TYPES):
            print('str test')
            a.fit(pd.DataFrame(X_test_df['str']), pd.DataFrame(Y_test_df))

        print('SUCCESS object test')
    except Exception as e:
        print(e)
        return False, "data object exception: " + str(e)

    try:
        if Algorithm.InputTypes.INT.value in Algorithm.get_input_types(a.INPUT_TYPES):
            print('int test')
            a.fit(pd.DataFrame(X_test_df['int']), pd.DataFrame(Y_test_df))

        print('SUCCESS int test')
    except Exception as e:
        print(e)
        return False, "data int exception: " + str(e)

    try:
        if 'bool' in Algorithm.get_input_types(a.INPUT_TYPES):
            print('bool test')
            a.fit(pd.DataFrame(X_test_df['bool']), pd.DataFrame(Y_test_df))

        print('SUCCESS bool test')
    except Exception as e:
        print(e)
        return False, "data bool exception: " + str(e)

    try:
        if Algorithm.PreReq.NOT_NULL.value not in Algorithm.get_input_types(a.PRE_REQ):
            a.fit(X_test_df['none'], Y_test_df)

        print('SUCCESS Null test')
    except Exception as e:
        print(e)
        return False, "not Null exception: " + str(e)

    print('SUCCESS DATA TEST')
    return True, 'SUCCESS'


def parse(name: str):
    """
    Функция для тестирования алгоритма

    :param name: название файла с алгоритмом
    :return: {
        "status": True,
        "details": "exception",
        "name": "db_mane",
        "desc": "desc",
        "pre": []
    }
    """

    alg = get_alg_by_file_name(name, algs_loader('test'))
    test_result = alg_test(alg())

    return {
        "status": test_result[0],
        "details": test_result[1],
        "name": alg.ALGORITHM_NAME,
        "desc": alg.DESCRIPTION,
        "pre": alg.PRE_REQ
    }
    pass

# TODO: затестить все параметры, все значения set + Min и Max (опасно)
