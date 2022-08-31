'''
И снова нейросеть (известная нам с прошлых уроков)
x * w1 + w0

и тренировочная выборка
x   y
0   1
1   2
2   3

Для человека не составит труда восстановить зависимость между x и y. Ну да, y=x+1. То есть оптимальные значения весов сети w1 = 1; w0 = 1. Посмотрим, сумеет ли нейронная сеть обнаружить эти значения в процессе тренировки.
В этой задаче мы будем применять регуляризацию, а именно: припишем к "обычной" функции потерь L(w) "хвост" + C(w0^2 + w1^2), где в качестве константы С мы возьмем С=1.
После этого начинаем обычную процедуру градиентного спуска.
Для старта спуска возьмем a0=(0,0); h=0.1, причем мы предполагаем, что первая координата позиции "шарика" соответствует весу w0, а вторая координата соответствует весу w1.
Давайте сделаем два шага градиентного спуска и получим позицию a2.
В окошко ответа запишите первую координату (которая соответствует весу w0) позиции a2.
Ну как? Стала ли позиция "шарика" a2 ближе к точке истинной минимума функции потерь (1,1)? Быстрее или медленнее теперь (то есть и с использованием регуляризации) веса стремятся к оптимальным значениям? Сравните свой ответ с ответом аналогичной задачи, которая решалась без использования регуляризации.
Спойлер: на самом деле веса медленнее сходятся к оптимальным значениям. Мешает регуляризация, ибо она негодует, когда веса нейросети увеличиваются (по модулю).
'''

'''
Градиентный спуск
a = a - f'(a) * h

Фн потерь
Lw = (Fnn(x1) - y1)^2 + (Fnn(x2) - y2)^2 + (Fnn(x3) - y3)^2

Lw = (w0 - 1)**2 + (w1 + w0 - 2)**2 + (2*w1 + w0 - 3)**2 + 1*(w0**2 + w1**2)
'''

from sympy import diff, lambdify, symbols, pprint

trainSelection = [
    [0, 1],
    [1, 2],
    [2, 3],
]

def lostFn(a0, a1, h, iterations):
    w0, w1 = symbols('w0 w1')
    Lw = (w0 - 1)**2 + (w1 + w0 - 2)**2 + (2*w1 + w0 - 3)**2 + 1*(w0**2 + w1**2)

    d0 = diff(Lw, w0)
    d1 = diff(Lw, w1)

    pprint(d0)
    pprint(d1)

    l0 = lambdify([w0, w1], d0)
    l1 = lambdify([w0, w1], d1)

    for i in range(iterations):
        _a0 = a0 - h * l0(a0, a1)
        _a1 = a1 - h * l1(a0, a1)
        a0, a1 = _a0, _a1
        print(
            'step', i+1,
            'a0', round(a0, 2),
            'a1', round(a1, 2),
        )

    pass

def main():
    lostFn(0, 0, 0.1, 5)

if __name__ == '__main__':
    main()





