'''
Планируется разбить объекты на 2 кластера На первой итерации работы алгоритма k-means были выбраны точки (2,3) и (1,1). После первой итерации алгоритма к кластеру, определяемому первой точкой, будут отнесены объекты (используется метрика Манхэттен)...
'''

class KMeansGen:
    def __init__(self):
        self.objects = {
            'A': [4, 2],
            'B': [3, 2],
            'C': [1, -1],
            'D': [-1, 1],
            'E': [0, 4],
        }
        self.k1 = [2, 3]
        self.k2 = [1, 1]

    def getDistance(self, p, k):
        return abs(p[0] - k[0]) + abs(p[1] - k[1])

    def getCentre(self, points):
        x = 0
        y = 0
        for point in points:
            x += self.objects[point][0]
            y += self.objects[point][1]
        return (x / len(points), y / len(points))


    def getNewK(self):
        pointsK1 = []
        pointsK2 = []

        for point in self.objects.keys():
            distK1 = self.getDistance(self.objects[point], self.k1)
            distK2 = self.getDistance(self.objects[point], self.k2)
            if distK1 < distK2:
                pointsK1.append(point)
            else:
                pointsK2.append(point)

        self.k1 = self.getCentre(pointsK1)
        self.k2 = self.getCentre(pointsK2)

        print(
            'pointsK1', pointsK1,
            'pointsK2', pointsK2,
        )


def main():
    km = KMeansGen()
    km.getNewK()

if __name__ == '__main__':
    main()
