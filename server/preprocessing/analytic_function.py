import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def class_count(label):
    label.value_counts()

def atribute_distribution(atribute):
    plt.hist(atribute, color='blue', edgecolor='black',
             bins=int(180 / 5))

def correlation_hotmap(data, label):
    pass

def miss_values_count(data):
    data.isnull().sum()
    pass

def data_types(data):
    print(data.dtypes)