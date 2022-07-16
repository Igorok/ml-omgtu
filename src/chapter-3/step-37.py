'''
Заполните пропуски
В данной задаче выбросы будем искать по следующему правилу: «Выбросом будет считаться объект, у которого суммарное расстояние от него до остальных объектов выборки наибольшее». Таким образом, в указанной таблице выбросом будет (написать имя объекта в виде заглавной латинской буквы): ... (при вычислении использовать метрику Манхэттен, нормализацию не проводить), сумма расстояний от него до остальных объектов будет равна ...

    P1  P2  P3
A   1   1   0
B   0   2   -1
C   2   3   1
D   1   0   4
'''

class OutlierDetecter:
    def __init__(self):
        self.objects = {
            'A': (1, 1, 0),
            'B': (0, 2, -1),
            'C': (2, 3, 1),
            'D': (1, 0, 4),
        }
        self.metrics = {}
        self.totalMetric = {}

    def calculate(self):
        objLen = len(self.objects.keys())
        for i in range(objLen - 1):
            j = i + 1
            while j < objLen:
                k1 = list(self.objects.keys())[i]
                k2 = list(self.objects.keys())[j]
                metric = 0
                for pi in range(len(self.objects[k1])):
                    metric += abs(self.objects[k1][pi] - self.objects[k2][pi])

                if not k1 in self.metrics:
                    self.metrics[k1] = {}
                if not k2 in self.metrics:
                    self.metrics[k2] = {}

                self.metrics[k1][k2] = metric
                self.metrics[k2][k1] = metric

                if not k1 in self.totalMetric:
                    self.totalMetric[k1] = 0
                if not k2 in self.totalMetric:
                    self.totalMetric[k2] = 0

                self.totalMetric[k1] += metric
                self.totalMetric[k2] += metric

                j += 1

        return (self.metrics, self.totalMetric)


'''
{
    'A': {
        'B': 3,
        'C': 4,
        'D': 5
    },
    'B': {
        'A': 3,
        'C': 5,
        'D': 8
    },
    'C': {
        'A': 4,
        'B': 5,
        'D': 7
    },
    'D': {
        'A': 5,
        'B': 8,
        'C': 7
    }
}

{'A': 12, 'B': 16, 'C': 16, 'D': 20})
'''
def main():
    od = OutlierDetecter()
    print('od.calculate()', od.calculate())

if __name__ == '__main__':
    main()
