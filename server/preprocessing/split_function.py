from sklearn.model_selection import train_test_split


def sample_split(splits: list[dict], dataset) -> dict:
    """
    :param splits: лист с параметрами разбиения(ts - % разбиения, rs - коэффициент случайности, st - сохранение пропорций класса)
    :param dataset: обработанный датасет
    :return: массив словарей, содержащих разбиения выборки
    """
    n = dataset.shape[1]
    X = dataset.iloc[:, 1:n]
    Y = dataset.iloc[0]
    res = []
    for sp in splits:
        if "sz" in sp.keys() and "rs" in sp.keys():
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                                test_size=sp["ts"],
                                                                random_state=sp["rs"],
                                                                stratify=sp["st"])
        res.append({
            "trainX": X_train,
            "trainY": Y_train,
            "testX": X_test,
            "testY": Y_test,
        })
    return res
