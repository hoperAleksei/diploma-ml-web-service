from autoload import ModuleLoader

def algs_loader(folder: str):
    """
    :param folder: путь к папке
    :return: tuple классов
    """
    # print('start loading')
    loader = ModuleLoader()  # создание лоудера
    validator_classes = loader.load_classes(folder)  # смотрим в папку
    return validator_classes


def get_load_algs_names(classes):
    return [i.ALGORITHM_NAME for i in classes]


def get_alg_by_name(alg_name, classes):
    for i in classes:
        if i.ALGORITHM_NAME == alg_name:
            return i
    return None
