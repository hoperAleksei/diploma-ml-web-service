import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def class_count(label):
    label.value_counts().to_dict()

def atribute_distribution(atribute):
    return  plt.hist(atribute, color='blue', edgecolor='black', bins=int(180 / 5))

def correlation_hotmap(data):
    correlation_matrix = data.corr()
    plt.figure(figsize = (10, 6))
    return (sns.heatmap(correlation_matrix, annot = True))

def miss_values_count(data):
    return data.isnull().sum().to_dict()

def data_types(data):
    return data.dtypes.to_dict()