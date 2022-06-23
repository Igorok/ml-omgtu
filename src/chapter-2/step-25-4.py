'''
Дан вектор значений признака Р=(1,0,5,2,2). Нормализуем этот вектор по формуле, использующей среднее значением и отклонение признака Р. Значение последней координаты нормализованного вектора будет равно
'''

import pandas as pd

class Vector252:
    def __init__(self):
        self.P1 = (0,1,2)
        self.P2 = (2,1,0)

    def euclideanDistance(self):
        sumOfSquare = 0
        for i in range(3):
            sumOfSquare += (self.P1[i] - self.P2[i])**2
        return round(sumOfSquare**0.5, 2)

    def manhattan(self):
        sumOfAbs = 0
        for i in range(3):
            sumOfAbs += abs(self.P1[i] - self.P2[i])
        return sumOfAbs

    def maxMetric(self):
        diffs = [abs(self.P1[i] - self.P2[i]) for i in range(3)]
        return max(diffs)

class Vector253:
    def __init__(self):
        self.P = (1, 0, 5, 2, 2)
        self.df = pd.DataFrame(self.P)
        self.max = self.df.max()[0]
        self.min = self.df.min()[0]
        self.mean = self.df.mean().round(2)[0]
        self.std = self.df.std().round(2)[0]

    def normalizeMaxMin(self, value):
        return (value - self.min) / (self.max - self.min)

    def getNormalizedMaxMin(self):
        return list(self.normalizeMaxMin(self.P[i]) for i in range(len(self.P)))

    def normalizeMean(self, value):
        return round((value - self.mean) / self.std, 2)

    def getNormalizedMean(self):
        return list(self.normalizeMean(self.P[i]) for i in range(len(self.P)))


def main():
    vector252 = Vector252()
    print(
        'euclideanDistance', vector252.euclideanDistance(),
        'manhattan', vector252.manhattan(),
        'euclideanDistance', vector252.maxMetric()
    )

    vector253 = Vector253()
    print(
        'getNormalizedMaxMin', vector253.getNormalizedMaxMin(),
        'getNormalizedAverage', vector253.getNormalizedMean()
    )

if __name__ == '__main__':
    main()
