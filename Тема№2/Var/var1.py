#Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).

from itertools import count, islice


def iterator(n):
    if n > 0:
        if n == 1:
            print('[0]')
        elif n > 1:
            lis = [0, 1, ]
            for i in islice(count(2), n):
                lis.append(lis[i - 1] + lis[i - 2])
            return lis
    else:
        print('Проверьте число')


if __name__ == "__main__":
    
    n = int(input('Количество элементов: '))
    print(f'iterator({n}): \n', iterator(n))
