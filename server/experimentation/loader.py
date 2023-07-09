from autoload import ModuleLoader
from .algs.algorithm import Algorithm


def algs_loader(folder: str) -> tuple[Algorithm]:
    """
    Загрузчик алгоритмов

    :param folder: путь к папке
    :return: tuple классов
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


def get_alg_by_name(alg_name, classes):
    for i in classes:
        if i.ALGORITHM_NAME == alg_name:
            return i
    return None


def get_alg_by_file_name(file_name, classes):
    for cls in classes:
        if cls.__repr__(cls).split("'")[1].split(".")[0] == file_name:
            return cls
    return None


# print(get_alg_by_file_name('knn', algs_loader('algs')))

def get_all_algs_req():
    """
    Получить требования всех алгоритмов:
    :return:
    """

    classes = algs_loader('algs')
    out_list = []

    for cls in classes:
        print(cls.ALGORITHM_NAME)
        a = cls
        out_list.append(Algorithm.get_alg_requirements(a))
    return out_list


def get_all_alg(classes_names: list):
    """
    :param classes_names: список имён алгоритмов
    """
    classes = algs_loader('algs')
    out_list = []

    for cls in classes:
        if cls.ALGORITHM_NAME in classes_names:
            out_list.append({
                "name": cls.ALGORITHM_NAME,
                "params": cls.PARAMS
            })

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
