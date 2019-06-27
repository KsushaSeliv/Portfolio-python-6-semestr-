#Графики

%matplotlib inline
import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('ex1data1.csv', header = None) #Загружаем данные из csv-файла в скрипт с помощью метода read_csv модуля pandas.
x, y = df[0], df[1]
x1=[1,25]
y1=[0,25]
#t = arange(0.0, 25.0, 0.01)
fig = plt.figure()                 
pl1 = plt.subplot(111) #с subplot нарисуем на этом же графике кривую, «соответствующую» данным, считанным из файла. Пусть эта будет линия, соответствующая графику функции y = 2*x-10

plt.plot(x, y, 'b*') #Используя метод plot визуализируем данные, считанные из файла.
pl1.plot(x1, y1, 'g-') 


#pl1.plot(t,(2*t-10),'g-')


#Алгоритм градиентного спуска для линейной регрессии с одной переменной.

def odinspusk(X, Y, koef, n): #вычисляем theta0 и theta1 
    l = len(x)
    theta0, theta1 = 0, 0
    for i in range(n):
        sum1 = 0
        for i in range(l):
            sum1 += theta0 + theta1 * x[i] - y[i]
        res1 = theta0 - koef * (1 / l) * sum1

        sum2 = 0
        for i in range(l):
            sum2 += (theta0 + theta1 * x[i] - y[i]) * x[i]
        res2 = theta1 - koef * (1 / l) * sum2

        theta0, theta1 = res1, res2

    return theta0, theta1

x2 = [1, 25]
y2 = [0, 0]
t0, t1 = odinspusk(x, y, 0.01, len(x))
y2[0] = t0 + x2[0] * t1
y2[1] = t0 + x2[1] * t1
plt.plot(x2, y2, 'y-')


#polyfit

nx = np.array(x) #создаём два новых массива
ny = np.array(y)

nt1, nt0 = np.polyfit(nx, ny, 1) #p = polyfit(x,y,n) функция позволяет рассчитать коэффициенты
                                                     #p полиномиальной регрессионной модели n-й степени для выборки x,
                                                     #y методом наименьших квадратов, где x - независимая переменная,
                                                     #y - зависимая переменная. Зависимая и независимая переменные
                                                    #задаются как векторы с одинаковым числом элементов. 

num_y1 = [0, 0]
num_y1[0] = nt0 + x1[0] * nt1
num_y1[1] = nt0 + x1[1] * nt1
plt.plot(x1, num_y1, 'b-')



plt.plot(x, y, 'b*')
plt.plot(x2, y2, 'y-')
plt.plot(x1, num_y1, 'b-')


#Линейная регрессия со множеством переменных

df2 = pd.read_csv('webtraffic.csv', header = None) 
l, k = df2[0], df2[1]

lis = list(l)
lis2 = list(k)

plt.plot(l, k, 'm*')


for i in range(len(lis2)):
    if math.isnan(lis2[i]): #является ли i NaN (Not a Number - не число)

        lis2[i] = 0
    else:
        lis2[i] = lis2[i]

np_x = np.array(lis) #создаём два новых массива
np_y = np.array(lis2)


x2 = list(range(743))

th1_1, th0_1 = np.polyfit(np_x, np_y, 1)
th2_2, th1_2, th0_2 = np.polyfit(np_x, np_y, 2)
th3_3, th2_3, th1_3, th0_3 = np.polyfit(np_x, np_y, 3)
th4_4, th3_4, th2_4, th1_4, th0_4 = np.polyfit(np_x, np_y, 4)
th5_5, th4_5, th3_5, th2_5, th1_5, th0_5 = np.polyfit(np_x, np_y, 5)

f1 = lambda x: th1_1*x + th0_1
f2 = lambda x: th2_2*x**2 + th1_2*x + th0_2
f3 = lambda x: th3_3*x**3 + th2_3*x**2 + th1_3*x + th0_3
f4 = lambda x: th4_4*x**4 + th3_4*x**3 + th2_4*x**2 + th1_4*x + th0_4
f5 = lambda x: th5_5*x**5 + th4_5*x**4 + th3_5*x**3 + th2_5*x**2 + th1_5*x + th0_5


f6 = np.poly1d(np.polyfit(np_x, np_y, 1)) #Удобный класс, используемый для инкапсуляции «естественных» операций над полиномами,
                                          #чтобы указанные операции могли принять свою обычную форму в коде.
plt.plot(x2, f6(x2))
f7 = np.poly1d(np.polyfit(np_x, np_y, 2))
plt.plot(x2, f7(x2))
f8 = np.poly1d(np.polyfit(np_x, np_y, 3))
plt.plot(x2, f8(x2))
f9 = np.poly1d(np.polyfit(np_x, np_y, 4))
plt.plot(x2, f9(x2))
f10 = np.poly1d(np.polyfit(np_x, np_y, 5))
plt.plot(x2, f10(x2))


plt.plot(l, k, 'y*')
plt.plot(x2, f6(x2))
plt.plot(x2, f7(x2))
plt.plot(x2, f8(x2))
plt.plot(x2, f9(x2))
plt.plot(x2, f10(x2))


#Чуть не забыли
def srqvadr(sqx, sqy, f_x=None):  #Вычисление среднеквадратичной ошибки
    srqvadr = []
    for i in range(len(sqx)):
        srqvadr.append((f_x(sqx[i]) - sqy[i])**2)
    return sum(srqvadr)

print("Ср.кв.откл.", srqvadr(lis, lis2, f1))
print("Ср.кв.откл.", srqvadr(lis, lis2, f2))
print("Ср.кв.откл.", srqvadr(lis, lis2, f3))
print("Ср.кв.откл.", srqvadr(lis, lis2, f4))
print("Ср.кв.откл.", srqvadr(lis, lis2, f5))





#Другая версия градиентного спуска
#Графики

%matplotlib inline
from scipy.misc import derivative
import pandas as pd 
from matplotlib import pylab as plt

# определяем функцию
def f(x):
    return (2*x-10)

# проверяем нахождение f'(x)
derivative(f, 0)


df = pd.read_csv('ex1data1.csv', header = None) #Загружаем данные из csv-файла в скрипт с помощью метода read_csv модуля pandas.
x, y = df[0], df[1]
x1 = list(x)
y1 = list(y)

for i in range(len(x1)):
    yn = f(x1[i])

Y = {x[i]: yn}
step=0.01
# по формуле градиентного спуска получаем все значения x y
for i in range(len(y1)):
    x1[i] = x1[i] - step*derivative(f, x1[i])
    yn = f(x1[i])
    Y[x1[i]] = yn


# наносим найденные точки на график
plt.plot(list(Y.keys()), list(Y.values()), 'r-')
plt.show()




