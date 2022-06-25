'''
По строкам отложены наименования товаров, а столбцы — номера заказов (в ячейке стоит 1, если товар входит в соответствующий заказ; 0 — в противном случае). При построении рекомендательной системы необходимо оценить степень похожести товаров с помощью вычисления евклидовой метрики. Наиболее похожим (близким) на товар А будет товар С и расстояние между этими товарами равно ... (ответ округлить до сотых).
'''

class GoodsPredictor:
    def __init__(self):
        self.goods = [ 'A', 'B', 'C', 'D' ]
        self.ordersByGoods = {
            'A': [1, 0, 1, 0, 1, 0],
            'B': [0, 1, 1, 1, 0, 0],
            'C': [1, 1, 0, 1, 1, 0],
            'D': [1, 1, 0, 1, 1, 1],
        }
        self.distances = {}

    def euclideanDist(self, list1, list2):
        sum = 0
        for i in range(len(list1)):
            sum += (list1[i] - list2[i]) ** 2
        return round(sum ** 0.5, 2)

    def generateDistance(self):
        for i in range(len(self.goods) - 1):
            j = i + 1
            while j < len(self.goods):
                goodI = self.goods[i]
                goodJ = self.goods[j]
                comparedGoods = goodI + goodJ
                self.distances[comparedGoods] = self.euclideanDist(
                    self.ordersByGoods[goodI],
                    self.ordersByGoods[goodJ],
                )
                j += 1

    def getNearest(self, good):
        minRel = None
        for relation in self.distances.keys():
            if good not in relation:
                continue
            if minRel == None:
                minRel = relation
            elif self.distances[minRel] > self.distances[relation]:
                minRel = relation
        return [minRel, self.distances[minRel]]

def main():
    goodsPredictor = GoodsPredictor()
    goodsPredictor.generateDistance()
    nerarest = goodsPredictor.getNearest('A')
    print('nerarest', nerarest)

if __name__ == '__main__':
    main()
