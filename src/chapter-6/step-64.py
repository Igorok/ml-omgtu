'''
Один очень тупой классификатор С относит все объекты к классу 1. Допустим,что выборка состоит из 50 объектов: 20 из них действительно принадлежат классу 0, а 30 из них действительно принадлежат классу 1.
Каждый из объектов выборки был подан классификатору С, в результате работы которого была заполнена матрица ошибок, в которой общая точность (accuracy) равна ..., precision = ..., recall = ...
'''

'''
Правильное распределение
    0   1
0   20  0
1   0   30

Классификатор
    0   1
0   0   0
1   20  30

Общая точность (accuracy): (TN+TP)/(TN+TP+FN+FP)
точность (precision): TP/(TP+FP)
полнота (recall): TP/(TP+FN)

accuracy = 30/50 = 0,6
precision = 30/(30+20) = 0,6
recall = 30/30 = 1
'''

'''
По тренировочной выборке из 70 элементов был построен некоторый классификатор. Мы взяли и проверили его качество на тестовой выборке, состоящей из 30 элементов. Сумма чисел TP+FP+FN+TN из матрицы ошибок равна

30=TP+FP+FN+TN=30
'''

'''
Даны объекты тренировочной выборки. На вход алгоритму kNN подается объект F с признаками X1=0, X2=0.
При k=3 объект F будет отнесен к классу ... При k=5 объект F будет отнесен к классу ... При решении задачи использовать евклидову метрику, нормализацию данных не проводить.

'''