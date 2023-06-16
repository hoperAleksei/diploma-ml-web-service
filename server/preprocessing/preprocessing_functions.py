from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

def convert_types(data):
    for name, values in data.items():
        if (values.dtypes == 'int64'):
            data[name] = data[name].astype('float64')
        if (values.dtypes == 'O'):
            try:
                data[name] = data[name].astype('float64')
            except ValueError:
                print(f"{name}: fail convert to float64")

def del_columns(data, columns):
    x = data
    for name in columns:
        x = x.drop([name], axis=1)
    return x

#Encoding

#функция кодирования категориальных признаков LabelEncoding
def AttributeLabelEncoder(data):
  for name, values in data.items():
    if (values.dtypes == 'O'):
      labelencoder = LabelEncoder()
      attribute_new = labelencoder.fit_transform(values)
      data[name] = attribute_new

#функция кодирования категориальных признаков One-HoteEncoding
def AttributeOneHotEncoder(data):
  for name, values in data.items():
    if (values.dtypes == 'O'):
      onehotencoder = OneHotEncoder()
      data_new = onehotencoder.fit_transform(data[[name]])
      data_new = pd.DataFrame(data_new.toarray(),
      columns=onehotencoder.categories_)
      data.drop(name, axis= 1 , inplace= True )
      data = data.join(data_new)


from category_encoders.binary import BinaryEncoder
#функция кодирования категориальных признаков BinaryEncoder
from category_encoders.binary import BinaryEncoder
def AttributeBinaryEncoder(data):
  for name, values in data.items():
    if (values.dtypes == 'O'):
      binaryencoder = BinaryEncoder()
      data_new = binaryencoder.fit_transform(data[[name]])
      data.drop(name, axis= 1 , inplace= True )
      data = data.join(data_new)


#Normalize

#функция нормализации данных
from sklearn.preprocessing import LabelEncoder
def NormalizeAttributes(data, label_name):
  for name, values in data.items():
    if (values.dtypes != 'O' and name != label_name):
      value_array = np.array(data[name])
      normalized_attribute = preprocessing.normalize([value_array])
      data[name] = normalized_attribute[0]

#функция min-max нормализации данных
from sklearn.preprocessing import LabelEncoder
def MinMaxNormalizeAttributes(data, label_name):
  for name, values in data.items():
    if (values.dtypes != 'O' and name != label_name):
      value_array = np.array(data[name])
      min_max_scaler = preprocessing.MinMaxScaler()
      normalized_attribute = min_max_scaler.fit_transform(np.transpose([value_array]))
      data[name] = np.transpose(normalized_attribute)[0]

def ZScoreNormalizeAttributes(data, label_name):
  for name, values in data.items():
    if (values.dtypes != 'O' and name != label_name):
      data[name] = (data[name] - data[name].mean()) / data[name].std()

def MaxAbsoluteScalingNormalizeAttributes(data, label_name):
  for name, values in data.items():
    if (values.dtypes != 'O' and name != label_name):
      data[name] = data[name] / data[name].abs().max()

# Обработка пропусков
def DelNanRow(data):
  d = data.dropna()
  d.reset_index(drop=True)
  return d

def DelNanColumn(data):
  d = data.dropna(axis=1)
  d.reset_index(drop=True)
  return d

#Функция замены на среднее и моду
def AvgReplaseData(data):
  d = data
  for name, values in d.items():
    if (values.dtypes == 'O'):
      d[name].fillna(d[name].mode(dropna=True)[0], inplace=True)
    if (values.dtypes == 'Int64'):
      d[name].fillna((round(d[name].mean(skipna=True))), inplace=True)
    if (values.dtypes == 'float64'):
      d[name].fillna((d[name].mean(skipna=True)), inplace=True)
  return d

#Функция замены на медиану и моду
from sklearn.preprocessing import LabelEncoder
def MedianReplaseData(data):
  d = data
  for name, values in d.items():
    if (values.dtypes == 'O'):
      d[name].fillna(d[name].mode(dropna=True)[0], inplace=True)
    if (values.dtypes == 'Int64'):
      d[name].fillna((round(d[name].median(skipna=True))), inplace=True)
    if (values.dtypes == 'float64'):
      d[name].fillna((d[name].median(skipna=True)), inplace=True)
  return d

# Обработка выбросов

def IQR(data):
  for name, values in data.items():
    if (values.dtypes == 'float64' or values.dtypes == 'Int64'):
      dataNotNull = data[name].dropna()
      q75,q25 = np.percentile(dataNotNull,[75,25])
      intr_qr = q75-q25

      max = q75+(1.5*intr_qr)
      min = q25-(1.5*intr_qr)

      data.loc[data[name] < min,name] = np.nan
      data.loc[data[name] > max,name] = np.nan


def StandardDeviations(data):
    for name, values in data.items():
        if (values.dtypes == 'float64' or values.dtypes == 'Int64'):
            data_std = np.std(data[name])
            data_mean = np.mean(data[name])
            anomaly_cut_off = data_std * 3

            lower_limit = data_mean - anomaly_cut_off
            upper_limit = data_mean + anomaly_cut_off
            data.loc[data[name] < lower_limit, name] = np.nan
            data.loc[data[name] > upper_limit, name] = np.nan

# Отбор признаков

import seaborn as sns
import matplotlib.pyplot as plt
#Предварительно необходим encoding, работает только с числовыми значениями
#Функция фильтрации на основе корреляции к label
#Возвращает новый дф, на доработку
def Corelation(data, label_name, attributeCount):
  correlation_matrix = data.corr()
  attributes = correlation_matrix[label_name].drop([label_name])
  attributes = attributes.abs().sort_values(ascending=False)
  d = pd.DataFrame()
  d = data[attributes.head(int(attributeCount)).index]
  d[label_name] = data[label_name]
  return d
