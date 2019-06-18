#Перемножение матриц с использованием потоков 


import threading #Модуль threading значительно упрощает работу с потоками
                 #и позволяет программировать запуск нескольких операций одновременно.

import numpy as np #поддержка больших многомерных массивов и матриц 

class Matric(threading.Thread): #мы хотим, чтобы класс работал как поток. 
                                #Для этого мы подклассифицируем свой класс из класса Thread . 
                                #Здесь Matric является дочерним классом класса Thread
    
    def __init__(self, potok, x, y, matr): #инициализация потока:num-номер потока,a-первая матрица,b-вторая матрица,
                                        #m_m-пустая строка, заполянется методом run
                                            
        threading.Thread.__init__(self) #конструктоор базового класса
        self.potok = potok
        self.A = A
        self.B = B
        self.matr = matr

    def run(self): #код внутри метода run() для запуска потока
        if self.potok is 0: #первый поток
            self.matr.append([])
            for i in range(3):
                self.matr[0].append(sum(self.A[0]*self.B[:,i])) #строка матрицы в виде списка * столбец матрицы в виде списка
                                                               #они поэлементно перемножаются и полученный список суммируется
                                                               #и получается одно число, которое мы записываем в 
                                                               #определённую ячейку нулевой строки новой матрицы  
        if self.potok is 1: #второй поток
            self.matr.append([])
            for i in range(3):
                self.matr[1].append(sum(self.A[1]*self.B[:,i]))
        if self.potok is 2: #третий поток
            self.matr.append([])
            for i in range(3):
                self.matr[2].append(sum(self.A[2]*self.B[:,i]))
            c = np.array(self.matr)
            
            print(f'A:\n{A}\n',f'B:\n{B}\n',f'AB:\n{c}')


A = np.array([(2, 7, 2), (1, 5, 9), (4, 2, 5)]) #вводим первую матрицу
B = np.array([(1, 2, 0), (3, 6, 2), (5, 8, 2)]) #вводит вторую матрицу
matricaitog = [] #здесь результат перемножения

for i in range(3):
    thread = Matric(i, A, B, matricaitog)
    thread.start()
