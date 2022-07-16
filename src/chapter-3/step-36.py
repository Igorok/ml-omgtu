'''
Первая и третья квартиль значений признака Р равны 2, 4 соответственно. Какие из следующих значений будут считаться выбросами?
'''

class Step1:
    def __init__(self):
        self.q25 = 2
        self.q75 = 4
        self.minBorder = self.q25 - 1.5 * (self.q75 - self.q25)
        self.maxBorder = self.q75 + 1.5 * (self.q75 - self.q25)
        self.values = (3, 0, 7.5, 6.5, 8, -1.5, 0.5)

    def isEjection(self, value):
        return (
            value < self.minBorder
            or value > self.maxBorder
        )

    def getEjections(self):
        return list(filter(self.isEjection, self.values))

'''
Среднее значение, отклонение и медиана десяти значений признака Р равны 10, 1.1 (одна целая одна десятая), и 9 соответственно. Какие из следующих значений будут выбросами? Не забудьте в процессе решения проверить симметричность выборки.
'''
class Step2:
    def __init__(self):
        self.mean = 10
        self.deviation = 1.1
        self.itemsLength = 10
        self.median = 9
        self.values = (13, 6, 7, 13.5, 6.5, 14)

    def isSymmetry(self):
        return self.median - self.mean <= 3 * ((self.deviation ** 2 / self.itemsLength) ** (1/2))

    def detectOutliers(self):
        isSym = self.isSymmetry()
        minV = 0
        maxV = 0
        if isSym:
            minV = self.mean - 3 * self.deviation
            maxV = self.mean + 3 * self.deviation
        else:
            minV = self.mean - 5 * self.deviation
            maxV = self.mean + 5 * self.deviation

        return list(filter(lambda val: (val < minV or val > maxV), self.values))


def main():
    step1 = Step1()
    print('step1.getEjections()', step1.getEjections())

    step2 = Step2()
    print('step2.detectOutliers()', step2.detectOutliers())

if __name__ == '__main__':
    main()
