'''
Свертка - небольшой фильтр гоняют по большому изображению, веса нейронов равны размеру фильтра. Используют для размытия изображений или выделения по границе

Сверточные нейронные сети
Размер после свертки -
(n-m+1) x (n-m+1)
'''

'''
Пусть фильтр 7х7 бегал по изображению 20х20. Какое количество строк будет у результата?
'''

'''
Будем гонять фильтр

1/9 1/9 1/9
1/9 1/9 1/9
1/9 1/9 1/9

по изображению

100001
011100
011100
111111
001100
101101

Какие будут размеры у результирующего изображения? Напишите количество строк у результата.
4
'''

'''
Берём условия последней задачи.
Сделайте операцию свёртки и получите результат.
Сколько ячеек в результирующем изображении равны 5/9 ?


[
    [0.5555555555555556, 0.6666666666666667, 0.4444444444444444, 0.3333333333333333],
    [0.7777777777777779, 1.0000000000000002, 0.7777777777777779, 0.5555555555555556],
    [0.6666666666666667, 0.8888888888888891, 0.7777777777777779, 0.5555555555555556],
    [0.6666666666666667, 0.7777777777777779, 0.7777777777777779, 0.6666666666666667]
]
'''

# convolution neural network
filterNn = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
]
matrixNn = [
    [1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1],
]

'''
[
    [5, 3, 5, 3, 5],
    [3, 4, 3, 4, 3],
    [5, 3, 5, 3, 5]
]

'''
filterStep4 = [
    [0,1,0],
    [1,1,1],
    [0,1,0],
]
matrixStep4 = [
    [0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1],
    [0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1],
    [0,1,0,1,0,1,0],
]


def convolutionNN(matrix, filter):
    rowSize = len(matrix[0]) - len(filter[0]) + 1
    result = []
    i = 0
    while (i + len(filter) <= len(matrix)):
        result.append([None]*rowSize)
        j = 0
        while (j + len(filter[0]) <= len(matrix[0])):
            r = 0
            print(
                'i', i,
                'j', j,
            )
            for x in range(len(filter)):
                for y in range(len(filter[0])):
                    r += matrix[i + x][j + y] * filter[x][y]
            result[i][j] = r
            j += 1
        i += 1

    print('result', result)


def getResSize(n,m):
    return n - m + 1

def main():
    print('getResSize', getResSize(20, 7))

    convolutionNN(matrixNn, filterNn)
    convolutionNN(matrixStep4, filterStep4)

if __name__ == '__main__':
    main()

