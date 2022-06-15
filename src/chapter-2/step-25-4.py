'''
Дан вектор значений признака Р=(1,0,5,2,2). Нормализуем этот вектор по формуле, использующей среднее значением и отклонение признака Р. Значение последней координаты нормализованного вектора будет равно
'''

import pandas as pd

P = [1,0,5,2,2]

def normal(value, mean, std):
    return (value - mean) / std

def main():
    df = pd.DataFrame(data={'p' : P})
    std = df.std()
    mean = df.mean()
    metric = normal(P[-1], mean, std)

    print('std', std, 'mean', mean, 'metric', metric)

    for i in range(len(P)):
        print('value', P[i], normal(P[i], mean, std))


if __name__ == '__main__':
    main()
