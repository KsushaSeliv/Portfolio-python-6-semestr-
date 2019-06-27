#Используя свободные источники (bn.ru, avito.ru и т.д.), собрать данные о ценах на недвижимость, выставленную на продажу
#в разных районах города. Преобразовать данные в формат csv. Разработать скрипт для визуализации данных, используя
#библиотеку matplotlib. Для визуализации использовать тип “точечная диаграмма” (scatterplot).


%matplotlib inline
import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('CENA.csv', header = None) #Загружаем данные из csv-файла в скрипт с помощью метода read_csv модуля pandas.
l, k = df[0], df[1]

plt.scatter(l, k, c ='black')

lis = list(l)
lis2 = list(k)
