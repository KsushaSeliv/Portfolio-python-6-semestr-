#Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.
#Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.


def vers(n):
    if n > 0:
        if n == 1:
            print('[0]')
        elif n > 1:
            res = [0] * n
            res[1] = 1
            for i in range(2, n):
                res[i] = res[i - 1] + res[i - 2]
            return res
    else:
        print('Проверьте число')


def vers2(n):
    if n > 0:
        if n == 1:
            print('[0]')
        elif n > 1:
            res = [0, 1, ]
            for i in range(2, n):
                res.append(res[i - 1] + res[i - 2])
            return res

    else:
        print('Проверьте число')


def fibonacci_generator(): 
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_iterator(n):
    it = iter(list(range(2, n)))
    res = [0, 1, ]
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        res.append(res[x - 1] + res[x - 2])
    return res


if __name__ == "__main__":
    n = int(input('Кол-во элементов: '))
    
    print(f'vers({n}): \n', vers(n))
    
    print(f'vers2({n}): \n', vers2(n))
    
    print(f'fibonacci_iterator({n}): \n', fibonacci_iterator(n))
    f = fibonacci_generator()
    result = []
    for x in range(n):
        result.append(f.__next__())
    print('Итератор2: \n', result)
