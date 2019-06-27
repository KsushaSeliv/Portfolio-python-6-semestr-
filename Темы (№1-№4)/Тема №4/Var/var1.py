#На основе кода, позволяющего визуализировать данные о ценах на недвижимость (точечная диаграмма),
#отобразить с помощью библиотеки matplotlib полиномиальный график (степеней полинома 3, 4, 10) изменений цен на недвижимость.

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

for i in range(len(lis2)):
    if math.isnan(lis2[i]): #является ли i NaN (Not a Number - не число)

        lis2[i] = 0
    else:
        lis2[i] = lis2[i]

np_x = np.array(lis) #создаём два новых массива
np_y = np.array(lis2)


x2 = list(range(743))

f1 = np.poly1d(np.polyfit(np_x, np_y, 3))
plt.plot(x2, f1(x2))
f2 = np.poly1d(np.polyfit(np_x, np_y, 4))
plt.plot(x2, f2(x2))
f3 = np.poly1d(np.polyfit(np_x, np_y, 10))
plt.plot(x2, f3(x2))
