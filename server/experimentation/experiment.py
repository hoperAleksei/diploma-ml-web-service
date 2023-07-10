import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, auc, roc_curve, f1_score
from itertools import product
import random
from .algs.algorithm import Algorithm
from .loader import get_load_algs_names, algs_loader, get_alg_by_name


def experiment_grid(params: dict, n_model: int = 10) -> list[dict]:
    """

    :param params: словарь параметров в формате
    params = {
        'n_neighbors': [1, 2, 3, 4, 5, 6],
        'weights': ['uniform', 'distance'],
    }
    :param n_model: максимальное число наборов гиперпараметров
    :return: наборы гиперпараметров в формате
    params = [
                {'n_neighbors': 6, 'weights': 'distance'},
                {'n_neighbors': 4, 'weights': 'uniform'},
                {'n_neighbors': 3, 'weights': 'uniform'},
                {'n_neighbors': 2, 'weights': 'uniform'}
    ]
    """
    out = []

    for i in params.keys():
        out.append(params[i])

    out_list = list(product(*out))
    out_dict = list(map(lambda x: {aa: x[j] for j, aa in enumerate(params.keys())}, out_list))

    if len(out_dict) > n_model:
        random.shuffle(out_dict)
        return out_dict[0:n_model]

    return out_dict


def int_param_generator(int_params: dict, n_steps: int = 10) -> list:
    """
        Генератор int параметров. генерирует с равномерным отступом от min к max.
        Если min = 1, max = 6, n_step = 2, то выход будет [1, 3, 6]

        :param int_params:  int параметр в формате
        {
            'type': 'int',
            'min': 1,
            'max': 30
        }
        :param n_steps: количество сгенерированных параметров
        :return: список сгенерированных параметров
        value_list = [1, 2, 3, ...]
    """
    if n_steps <= 0:
        n_steps = 1

    delta = int(int_params['max']) - int(int_params['min']) + 1
    if n_steps >= delta: n_steps = delta

    step = delta // n_steps
    current = int(int_params['min'])
    value_list = []
    while current <= int(int_params['max']):
        value_list.append(current)
        current += step
    return value_list


def float_param_generator(float_params: dict, n_steps: int = 10) -> list:
    """
    Генератор float параметров. генерирует случайный от min к max.
        Если min = 1, max = 6, n_step = 2, то выход будет [1, 3, 6]

    :param float_params: float параметр в формате
    {
        'type': 'float',
        'min': 1.0,
        'max': 2.0
    }

    :param n_steps:  количество сгенерированных параметров
    :return: список сгенерированных параметров
    value_list = [1.343, 1.942, 1.043, ...]
    """
    if n_steps <= 0:
        n_steps = 1

    delta = float(float_params['max']) - float(float_params['min'])

    value_list = []
    current = float(float_params['min'])

    for i in range(n_steps):
        value_list.append(round(current + delta * random.random(), 3))
    return value_list


def param_generator(params: dict, n_steps: int = 5) -> dict:
    """
    Генератор множеств гиперпараметров

    :param params: словарь параметров в формате
    {
    'n_neighbors': {
            'type': 'int',
            'min': 1,
            'max': 30
        },
    'weights': {
            'type': 'set',
            'values': ['uniform', 'distance']
        },
    'C': {
            'type': 'float',
            'min': 1,
            'max': 2
        }
    }
    :param n_steps: количество сгенерированных параметров каждого типа
    :return: словарь параметров в формате
    {
        'n_neighbors': [1, 2, 3, 4, 5, 6],
        'weights': ['uniform', 'distance'],
        'c': [1.2, 1.45, 1.14, ...]
    }
    """
    out_params = {}
    for i in params.keys():
        if params[i]['type'] == 'int':
            out_params[i] = int_param_generator(params[i], n_steps)

        if params[i]['type'] == 'float':
            out_params[i] = float_param_generator(params[i], n_steps)

        if params[i]['type'] == 'set':
            out_params[i] = list(params[i]['values'])
    return out_params


def experiment(algorithm: Algorithm, prams_values: list[dict],
               x_train: pd.DataFrame,
               y_train: pd.DataFrame,
               x_test: pd.DataFrame,
               y_test: pd.DataFrame) -> dict:
    """
    Запуск множества экспериментов по одному алгоритму

    :param y_test: метки класса тестовой выборки
    :param x_test: объекты тестовой выборки

    :param y_train: метки класса обучающей выборки
    :param x_train: объекты обучающей выборки

    :param algorithm: класс алгоритма с интерфейсом Algorithm
    :param prams_values: список наборов параметров для обучения в формате
    [
        {'n_neighbors': 6, 'weights': 'distance'},
        {'n_neighbors': 4, 'weights': 'uniform'},
        {'n_neighbors': 3, 'weights': 'uniform'},
        {'n_neighbors': 2, 'weights': 'uniform'}
    ]
    :return: результаты эксперимента (метрик) по всем наборам prams_values
    """
    exp_list = []

    for i in prams_values:
        model = algorithm(**{param_name: value for param_name, value in i.items()})
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)
        error_rate = 1 - accuracy
        precision = precision_score(y_test, y_pred, average='micro')
        recall = recall_score(y_test, y_pred, average='micro')
        f1 = f1_score(y_test, y_pred, average='micro')

        fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=0)
        roc_auc = auc(fpr, tpr)

        metric_dict = {
            "accuracy": round(accuracy, 3),
            "error_rate": round(error_rate, 3),
            "precision": round(precision, 3),
            "recall": round(recall, 3),
            "f1": round(f1, 3),
            "roc_auc": round(roc_auc, 3)
        }

        exp_dict = {
            "hyperparams": i,
            "metrics": metric_dict
        }

        exp_list.append(exp_dict)

    exp_out = {
        "alg_name": str(algorithm.ALGORITHM_NAME),
        "hyperparams_names": list(exp_dict['hyperparams'].keys()),
        "experiment": exp_list
    }
    return exp_out


def run_experiments(algs_and_params: list[dict],
                    x_train: pd.DataFrame,
                    y_train: pd.DataFrame,
                    x_test: pd.DataFrame,
                    y_test: pd.DataFrame) -> list[dict]:
    """
    Запуск множества экспериментов по заданным алгоритмам

    :param y_test: метки класса тестовой выборки
    :param x_test: объекты тестовой выборки

    :param y_train: метки класса обучающей выборки
    :param x_train: объекты обучающей выборки

    :param algs_and_params: список алгоритмов и ограничений их гиперпараметров
    [
        {
            'alg_name': 'knn',
            'n_steps': 5,
            'params':  {
                'n_neighbors': {
                        'type': 'int',
                        'min': 1,
                        'max': 30
                    },
                'weights': {
                        'type': 'set',
                        'values': ['uniform', 'distance']
                    },
                'C': {
                        'type': 'float',
                        'min': 1,
                        'max': 2
                    }
            }
        }, ...
    ]
    :return: список результатов по всем переданным алгоритмам [experiment(), ...]
    """

    # список экспериментов
    out_list = []

    # подгружать алгоритмы
    algs_list = algs_loader('algs')

    for i in algs_and_params:
        if i['alg_name'] in get_load_algs_names(algs_list):
            alg = get_alg_by_name(i['alg_name'], algs_list)

            # генерация параметров
            params = experiment_grid(param_generator(i['params'], i['n_steps']))

            # проведения экспериментов по всем параметрам
            out_list.append(experiment(alg, params, x_train, y_train, x_test, y_test))

    return out_list
