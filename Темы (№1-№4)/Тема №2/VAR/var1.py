#Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).

from itertools import count, islice

def itertoo(x):
    if x > 0:
        
        if x == 1:
            print('[0]')
        
        elif x > 1:
            ito = [0, 1, ]
            
            for i in islice(count(2), x):
                
                ito.append(ito[i - 1] + ito[i - 2])
                
            return ito
    else:
        print('Проверьте введённое число')

n = int(input('Кол-во элементов: '))

print(itertoo(n))
