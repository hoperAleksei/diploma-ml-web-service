import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def class_count(label: pd.Series) -> dict:
    """"
    :param label: Series с label
    :return: dict (key - название класса, value - колиечство)
    """
    return label.value_counts().to_dict()

def class_distribution(atribute: pd.Series) -> plt.hist:
    """"
    :param atribute: Series с параметром
    :return: plt.hist
    """
    return  plt.hist(atribute, color='blue', edgecolor='black', bins=int(180 / 5))

def correlation_hotmap(data: pd.DataFrame)  -> sns.heatmap:
    """"
    :param data: DataFrame
    :return: dsns.heatmap
    """
    correlation_matrix = data.corr()
    plt.figure(figsize = (10, 6))
    return sns.heatmap(correlation_matrix, annot = True)

def miss_values_count(data: pd.DataFrame) -> dict:
    """"
    :param data: DataFrame
    :return: dsns.heatmap
    """
    return data.isnull().sum().to_dict()

def data_types(data: pd.DataFrame) -> dict:
    """"
    :param data: DataFrame
    :return: dsns.heatmap
    """
    return data.dtypes.to_dict()