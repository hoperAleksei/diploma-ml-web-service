from pandas import DataFrame



PRE_TYPES = [{
    "type": "op",
    "name": "обработка пропусков",
    "methods": [
        {"name": "Удаление строк", "nm": "DelNanRow"},
        {"name": "Удаление столбцов", "nm":"DelNanColumn"},
        {"name": "Замена на среднее", "nm":"AvgReplaseData"},
        {"name": "Замена на медиану", "nm":"MedianReplaseData"}
    ]
},{
    "type": "ec",
    "name": "Категориальное кодирование",
    "methods": [
        {"name": "Label encoding", "nm":"AttributeLabelEncoder"},
        {"name": "One-hot encoding", "nm": "AttributeOneHotEncoder"},
        {"name": "Binary encoding", "nm":"AttributeBinaryEncoder"}
    ]
},{
    "type": "nd",
    "name": "Нормализация данных",
    "methods": [
        {"name": "Нормализация", "nm":"NormalizeAttributes"},
        {"name": "Min-max нормализация", "nm": "MinMaxNormalizeAttributes"},
        {"name": "Z-score", "nm":"ZScoreNormalizeAttributes"},
        {"name": "Максимальное абсолютное отклонение", "nm":"MaxAbsoluteScalingNormalizeAttributes"}
    ]
},{
    "type": "ov",
    "name": "Обработка выбросов",
    "methods": [
        {"name": "IQR", "nm":"IQR"},
        {"name": "Стандартное отклонение", "nm": "StandardDeviations"}
    ]
},{
    "type": "sa",
    "name": "Отбор признаков",
    "methods": [
        {"name": "Корреляция", "nm":"Corelation"},
        {"name": "КсиКвадрат", "nm": "ChiSquare"}
    ]
}
]

def preproc(data_set: DataFrame, pre_types: dict) -> DataFrame:
    return (data_set, pre_types)
    # raise NotImplemented
