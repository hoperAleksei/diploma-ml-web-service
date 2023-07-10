from autoload import ModuleLoader
from .algs.algorithm import Algorithm
from .schemas import get_all_alg_output


def algs_loader(folder: str) -> list[Algorithm]:
    """
    Загрузчик алгоритмов из папки folder

    :param folder: путь к папке
    :return: список классов алгоритмов
    """
    print('start loading')
    loader = ModuleLoader()  # создание лоудера
    validator_classes = loader.load_classes(folder)  # смотрим в папку

    validator_classes = list(validator_classes)

    for i in validator_classes:
        if i.ALGORITHM_NAME is None:
            validator_classes.remove(i)

    print(validator_classes)
    return validator_classes


def get_load_algs_names(classes: tuple[Algorithm]) -> list[str]:
    """
    Получить имена алгоритмов

    :param classes: tuple классов полученный из algs_loader
    :return: список имён алгоритмов
    """
    return [i.ALGORITHM_NAME for i in classes]


def get_alg_by_name(alg_name: str, classes: list[Algorithm]) -> Algorithm | None:
    """
    Получит алгоритм по его имени (ALGORITHM_NAME)
    Если не нашёл, то возвращает None

    :param alg_name: имя алгоритма (ALGORITHM_NAME)
    :param classes: список классов из algs_loader
    :return: искомый класс из classes | None
    """

    for i in classes:
        if i.ALGORITHM_NAME == alg_name:
            return i
    return None


def get_alg_by_file_name(file_name: str, classes: list[Algorithm]) -> Algorithm | None:
    """
    Получит алгоритм по имени его файла
    Если не нашёл, то возвращает None

    :param file_name: имя файла без расширения
    :param classes: список классов из algs_loader
    :return: искомый класс из classes | None
    """
    for cls in classes:
        if cls.__repr__(cls).split("'")[1].split(".")[0] == file_name:
            return cls
    return None


def get_all_algs_req() -> list:
    """
    Получить требования всех алгоритмов:
    :return: список требований в формате
    [
        {
                'alg_name': cls.ALGORITHM_NAME,
                'requirements': {
                    'NOT_NULL': Algorithm.PreReq.NOT_NULL in cls.PRE_REQ,
                    'NUM': Algorithm.PreReq.NUM in cls.PRE_REQ,
                    'NORM': Algorithm.PreReq.NORM in cls.PRE_REQ
                }
        }, ...
    ]
    """

    classes = algs_loader('algs')
    out_list = []

    for cls in classes:
        print(cls.ALGORITHM_NAME)
        a = cls
        out_list.append(Algorithm.get_alg_requirements(a))
    return out_list


def get_all_alg(classes_names: list) -> list[dict]:
    """
    :param classes_names: список имён алгоритмов
    :return: список в формате
    [
        {
            "name": 'Decision Tree',
            "params": {
                'max_depth': {
                    'type': 'int',
                    'min': '1',
                    'max': '100',
                    'decs': 'Максимальная глубина дерева'
                },
                'criterion': {
                    'type': 'set',
                    'values': ['gini', 'entropy', 'log_loss'],
                    'decs': 'Функция разделения'
            }
        },...
    ]
    """
    classes = algs_loader('algs')
    out_list = []

    for cls in classes:
        if cls.ALGORITHM_NAME in classes_names:
            out_list.append(get_all_alg_output.parse_obj({
                "name": cls.ALGORITHM_NAME,
                'desc': cls.DESCRIPTION,
                "params": cls.PARAMS
            }))

    return out_list

# def get_all_alg(PRED: list):
#     return [
#         {
#             "name": "alg1",
#             "params": [
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
#         }
#     ]
#

# def parse():
#     pass
