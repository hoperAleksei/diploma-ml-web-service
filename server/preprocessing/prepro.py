from pandas import DataFrame



PRE_TYPES = [
    {
        "name": "omis",
        "name_repr": "Обработка пропусков",
        "methods": [
            {"name": "rem_str", "name_repr": "Удаление строк"}
        ]
    },
    {
        "name": "norm",
        "name_repr": "Нормализация",
        "methods": [
            {"name": "rem_str", "name_repr": "Минмакс"}
        ]
    }
]

def preproc(data_set: DataFrame, pre_types: dict) -> DataFrame:
    raise NotImplemented
