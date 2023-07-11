from pandas import DataFrame
from preprocessing import preprocessing_functions as pf

PRE_TYPES = [{
    "type": "op",
    "name": "Обработка пропусков",
    "methods": [
        {"name": "Удаление строк", "nm": "DelNanRow"},
        {"name": "Удаление столбцов", "nm": "DelNanColumn"},
        {"name": "Замена на среднее", "nm": "AvgReplaseData"},
        {"name": "Замена на медиану", "nm": "MedianReplaseData"}
    ],
    "desc": "Очищает выборку от пропущенных значений"
}, {
    "type": "ec",
    "name": "Категориальное кодирование",
    "methods": [
        {"name": "Label encoding", "nm": "AttributeLabelEncoder"},
        {"name": "One-hot encoding", "nm": "AttributeOneHotEncoder"},
        {"name": "Binary encoding", "nm": "AttributeBinaryEncoder"}
    ],
    "desc": "Заменяет категориальные значения числовыми"
}, {
    "type": "nd",
    "name": "Нормализация данных",
    "methods": [
        {"name": "Нормализация", "nm": "NormalizeAttributes"},
        {"name": "Min-max нормализация", "nm": "MinMaxNormalizeAttributes"},
        {"name": "Z-score", "nm": "ZScoreNormalizeAttributes"},
        {"name": "Максимальное абсолютное отклонение", "nm": "MaxAbsoluteScalingNormalizeAttributes"}
    ],
    "desc": "Приводит данные в единный масштаб"
}, {
    "type": "ov",
    "name": "Обработка выбросов",
    "methods": [
        {"name": "IQR", "nm": "IQR"},
        {"name": "Стандартное отклонение", "nm": "StandardDeviations"}
    ],
    "desc": "Очищает выборку от сильно не типичных значений класса"
}, {
    "type": "sa",
    "name": "Отбор признаков",
    "methods": [
        {"name": "Корреляция", "nm": "Correlation"},
        {"name": "КсиКвадрат", "nm": "ChiSquare"}
    ],
    "value": "Число",
    "desc": "Оставляет N наиболее значимых признаков"
}, {
    "type": "de",
    "name": "Удаление признака",
    "value": "Лист признаков",
    "desc": "Удаляет выбранные признаки"
}, {
    "type": "tn",
    "name": "Замена значений на Nan",
    "value": "Лист значений",
    "desc": "Заменяет выбранные значения на Nan"
}
]

#Проверяет параметры датафрейма
def data_param(data: DataFrame) -> list:
    """
    :param data: Датасет
    :return: список, параметров датасета, для алгоритмов
    """
    norm = True
    num = True
    not_null = data.isnull().values.any()
    for name, values in data.items():
        if (values.dtypes == 'O'):
            num = False
            break
    for name, values in data.items():
        if (values.dtypes != 'O'):
            if (values.max() > 1 or values.min() < -1):
                norm = False
                break
    return [not_null, num, norm]

#Записывает алгоримтмы с статусом
def list_alg(data: DataFrame, alg_req: dict) -> list:
    """
    :param data: Датасет
    :return: список, из словарей ключ – название алгоритма, значение – статус
    """
    data_par = data_param(data)
    algs = []
    check = True
    for alg in alg_req:
        status = "ok"
        if (alg["requirements"]["NOT_NULL"] == True and data_par[0] == False):
           status = "not"
        if (alg["requirements"]["NUM"] == True and data_par[1] == False):
            status = "not"
        if (alg["requirements"]["NORM"] == True and data_par[2] == False):
            status = "not"
        algs.append({alg["alg_name"]:status})
    return algs

def preproc(data_set: DataFrame, pre_types: dict) -> list:
    """
    :param data_set: Выборка данных
    :param pre_types: словарь с методами предобработки и меткой
    :return: список, состоящий из признаков, метки и закодированной метки
    """

    try:
        res = [data_set]
        data_param(data_set)
        label = data_set[pre_types["label"]]
        data_set[pre_types["label"]] = pf.OneAttributeLabelEncoder(label)
        pf.convert_types(data_set)
        if "de" in pre_types.keys():
            data_set = pf.del_columns(data_set, pre_types["de"])
        if "tn" in pre_types.keys():
            data_set = pf.transform_value_to_nan(data_set, pre_types["tn"])
        if "op" in pre_types.keys():
            if ("DelNanRow" == pre_types["op"]):
                data_set = pf.DelNanRow(data_set)
            if ("DelNanColumn" == pre_types["op"]):
                data_set = pf.DelNanColumn(data_set)
            if ("AvgReplaseData" == pre_types["op"]):
                data_set = pf.AvgReplaseData(data_set)
            if ("MedianReplaseData" == pre_types["op"]):
                data_set = pf.MedianReplaseData(data_set)
        if "ec" in pre_types.keys():
            if ("AttributeLabelEncoder" == pre_types["ec"]):
                pf.AttributeLabelEncoder(data_set)
            if ("AttributeOneHotEncoder" == pre_types["ec"]):
                pf.AttributeOneHotEncoder(data_set)
                print(data_set)
            if ("AttributeBinaryEncoder" == pre_types["ec"]):
                pf.AttributeBinaryEncoder(data_set)
        if "nd" in pre_types.keys():
            if ("NormalizeAttributes" == pre_types["nd"]):
                pf.NormalizeAttributes(data_set, pre_types["label"])
            if ("MinMaxNormalizeAttributes" == pre_types["nd"]):
                pf.MinMaxNormalizeAttributes(data_set, pre_types["label"])
            if ("ZScoreNormalizeAttributes" == pre_types["nd"]):
                pf.ZScoreNormalizeAttributes(data_set, pre_types["label"])
            if ("MaxAbsoluteScalingNormalizeAttributes" == pre_types["nd"]):
                pf.MaxAbsoluteScalingNormalizeAttributes(data_set, pre_types["label"])
        if "ov" in pre_types.keys() and "op" in pre_types.keys():
            if ("IQR" == pre_types["ov"]):
                pf.IQR(data_set)
            if ("StandardDeviations" == pre_types["ov"]):
                pf.StandardDeviations(data_set)
            if ("DelNanRow" == pre_types["op"]):
                data_set = pf.DelNanRow(data_set)
            if ("DelNanColumn" == pre_types["op"]):
                data_set = pf.DelNanColumn(data_set)
            if ("AvgReplaseData" == pre_types["op"]):
                data_set = pf.AvgReplaseData(data_set)
            if ("MedianReplaseData" == pre_types["op"]):
                data_set = pf.MedianReplaseData(data_set)
        if "sa" in pre_types.keys() and "op" in pre_types.keys() and "ec" in pre_types.keys():
            if ("Correlation" == pre_types["sa"]):
                data_set = pf.Correlation(data_set, pre_types["label"], pre_types["count"])
        pf.convert_types(data_set)
        labelcode = data_set[pre_types["label"]]
        data_set.drop([pre_types["label"]], axis=1, inplace=True)
        res = [data_set, pre_types["label"], labelcode]
        return res
    except KeyError:
        raise Exception("key Error")
