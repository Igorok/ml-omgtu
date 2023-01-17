'''
Изучим страйды на примере известной вам задачи про кресты.
Фильтр:
010
111
010

Изображение:
0101010
1111111
0101010
1111111
0101010

Но теперь у нас stride_x=2, stride_y=1.
Подумайте, какой будет размер результирующего изображения?  В ответ запишите сумму значений всех ячеек.
'''

filterStep2 = [
    [0,1,0],
    [1,1,1],
    [0,1,0],
]
matrixStep2 = [
    [0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1],
    [0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1],
    [0,1,0,1,0,1,0],
]

def convolutionNN(matrix, filter, strideX, strideY):
    rowSize = len(matrix[0]) - len(filter[0]) + strideX
    result = []
    i = 0
    while (i + len(filter) <= len(matrix)):
        rowRes = []
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
            rowRes.append(r)
            j += strideX
        result.append(rowRes)
        i += strideY

    print('result', result)
    return result

def sumMatrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum += matrix[i][j]
    return sum

'''
Изучим паддинг.
Фильтр:
001
010
100

Изображение:
111
101
111

matrixStep5 [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
paddingToMatrix [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

'''

filterStep5 = [
    [0,0,1],
    [0,1,0],
    [1,0,0]
]
matrixStep5 = [
    [1,1,1],
    [1,0,1],
    [1,1,1],
]

def paddingToMatrix(matrix, padding):
    rowLen = len(matrix[0])
    newRowLen = rowLen + padding * 2
    emptyRow = [0] * newRowLen
    result = []
    for _ in range(padding):
        result.append(emptyRow)

    paddingRow = [0] * padding
    for row in matrix:
        newRow = paddingRow + row + paddingRow
        result.append(newRow)

    for _ in range(padding):
        result.append(emptyRow)

    return result

'''
Было изображение
110
011
110

К нему сначала применили фильтр
11 (это фильтр с 1й строкой и 2мя столбцами),
а потом фильтр
0
1
(это фильтр с 2мя строками и 1м столбцом).
'''

matrix15Step2 = [
    [1,1,0],
    [0,1,1],
    [1,1,0],
]

filter15Step21 = [[1,1]]
filter15Step22 = [
    [0],
    [1],
]

'''
Было изображение (как в предыдущей задаче)
110
011
110
Но теперь мы перевернем фильтры!
Сначала применим фильтр
1
1
(это фильтр с 2мя строками и 1м столбцом),
а потом фильтр
01
(это фильтр с 1й строкой и 2мя столбцами).
'''
filter15Step31 = [
    [1],
    [1],
]
filter15Step32 = [[0, 1]]

def getColumn(matrix, column):
    result = []
    for row in matrix:
        result.append([row[column]])

    print('column', result)
    return result

def main():
    convMatrixStep2 = convolutionNN(matrixStep2, filterStep2, 2, 2)
    sumStep2 = sumMatrix(convMatrixStep2)
    print('sumStep2', sumStep2)

    paddingMatrixStep5 = paddingToMatrix(matrixStep5, 1)
    convMatrixStep5 = convolutionNN(paddingMatrixStep5, filterStep5, 1, 1)
    sumStep5 = sumMatrix(convMatrixStep5)
    print('sumStep5', sumStep5)

    convMatrix15Step21 = convolutionNN(matrix15Step2, filter15Step21, 1, 1)
    convMatrix15Step22 = convolutionNN(convMatrix15Step21, filter15Step22, 1, 1)
    sum15Step2 = sumMatrix(convMatrix15Step22)
    print('sum15Step2', sum15Step2)

    convMatrix15Step31 = convolutionNN(matrix15Step2, filter15Step31, 1, 1)
    convMatrix15Step32 = convolutionNN(convMatrix15Step31, filter15Step32, 1, 1)
    columnStep3 = getColumn(convMatrix15Step32, 1)
    sum15Step3 = sumMatrix(columnStep3)
    print('sum15Step3', sum15Step3)

if __name__ == '__main__':
    main()





