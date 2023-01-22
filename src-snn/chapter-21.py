'''
Рассмотрим простейшую СНС (в ней всего один фильтр). Я надеюсь, что вы сможете выписать как величина a зависит от величин p_11,..., p_22, w_11,..., w_22.

Пусть нам дана такая тренировочная выборка:
Картинка Р  Y
00
00          0

10
01          2

11
11          4

00
01          1

Ну я думаю, что вы поняли закономерность: Y — это сумма значений пикселей картинки.
Допустим, что мы натренировали СНС, и она поняла истинную закономерность. Чему в этом случае будет равен вес w_11?
'''

'''
0*w11 + 0*w12 + 0*w21 + 0*w22 = 0
1*w11 + 0*w12 + 0*w21 + 1*w22 = 2
1*w11 + 1*w12 + 1*w21 + 1*w22 = 4
0*w11 + 0*w12 + 0*w21 + 1*w22 = 1
'''

'''
Пусть у нас есть изображение 6х6:

1 2 3 4 5 6
6 5 4 3 2 1
3 2 1 6 5 4
2 1 3 5 6 4
6 2 4 1 3 5
2 4 6 5 3 1

Что с ним будет после (2,3)-пулинга (каждый маленький прямоугольничек состоит из 2х строк и 3х столбцов)?
В качестве ответа запишите сумму всех ячеек результирующего изображения.
В задаче используется операция max-пулинга.

1 2 3   4 5 6
6 5 4   3 2 1

3 2 1   6 5 4
2 1 3   5 6 4

6 2 4   1 3 5
2 4 6   5 3 1

6 6
3 6
6 5

32
'''

'''
1 2     3 4     5 6
6 5     4 3     2 1

3 2     1 6     5 4
2 1     3 5     6 4

6 2     4 1     3 5
2 4     6 5     3 1

6 4 6
3 6 6
6 6 5

16 + 15 + 17

'''

'''
У изображения 2 канала:
1й канал:
010
111

2й канал:
110
011

К нему применяют двухканальный фильтр.
1й канал:
01
2й канал:
11
Что получится в итоге?
В ответ напишите сумму значений пикселей в результирующем изображении.
'''

'''
10
11

21
12

31
23
9
'''

'''
Перевернём фильтры из предыдущей задачи. Итак:
У изображения 2 канала:
1й канал:
010
111

2й канал:
110
011

К нему применяют двухканальный фильтр.
1й канал:
0
1

2й канал:
1
1

Что получится в итоге?
В ответ напишите сумму значений пикселей в результирующем изображении.
'''

'''
010 0
111 1

110 1
011 1

111

121

232
7
'''

'''
Вот вам данные задачи, которая будет обсасываться на следующих нескольких вкладках.
0. Было трёхканальное (привет, RGB) изображение размера 20х20.
1. К нему применили 5 фильтров (они, естественно, 3-канальные) размера 7х7.
2. Потом ко всем каналам применили 2-пулинг.
3. К полученному изображению применили 6 фильтров 3х3.
Всюду у фильтров stride_x=stride_y=1, padding=0.
'''

'''
Начинаем решать задачу с прошлой вкладки.
Рассмотрим первое преобразование:
0. Было трёхканальное (привет, RGB) изображение размера 20х20.
1. К нему применили 5 фильтров (они, естественно, 3-канальные) размера 7х7.
Сколько каналов будет в результирующем изображении и какова размерность одного канала? (это можете обсудить в комментариях)
Напишите в ответе количество возникающих на этом слое весов для тренировки

20х20
20х20
20х20

7х7
7х7
7х7

7х7
7х7
7х7

7х7
7х7
7х7

7х7
7х7
7х7

7х7
7х7
7х7

14х14
14х14
14х14
14х14
14х14


7*7*3*5
'''

'''
Теперь следующий этап обработки изображения:
2. Потом ко всем каналам применили 2-пулинг.
Что тут с весами для тренировки?
Какова размерность каждого канала после пулинга. Напишите это в ответ.

14х14
14х14
14х14
14х14
14х14

7x7
7x7
7x7
7x7
7x7
'''



'''
Рассмотрим следующее преобразование:
3. К полученному изображению применили 6 фильтров 3х3.
Сколько каналов будет в результирующем изображении и какова размерность одного канала? (это можете обсудить в комментариях)
Напишите в ответе количество весов для тренировки.

7x7
7x7
7x7
7x7
7x7

3x3
3x3
3x3
3x3
3x3
3x3

5x5
5x5
5x5
5x5
5x5
5x5

5*3*3*6
'''


















