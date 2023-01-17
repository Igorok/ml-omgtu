'''
Теперь освежим действие дропаута на входном слое следующей нейросети:
x1 * w1 + x2 * w2 + w0

Тренировочная выборка
x1  x2  y
0   0   0
0   1   0
1   0   0
1   1   1

очевидна для человека. Еще бы: Y = X1 * X2
Но посмотрим, к какой зависимости придет нейросеть с применением дропаута на входном слое.
Допустим, что вначале был удален вход x2.
Проведите одну итерацию градиентного спуска и напишите, чему будет равен вес w1.

Fnn = x1 * w1 + x2 * w2 + w0
Fnn1 = x1 * w1 + w0
Fnn2 = x2 * w2 + w0

Lw1 = (Fnn1(0) - 0)**2 + (Fnn1(0) - 0)**2 + (Fnn1(1) - 0)**2 + (Fnn1(1) - 1)**2
= w0**2 + w0**2 + (w1 + w0)**2 + (w1 + w0 - 1)**2

Lw2 = (Fnn2(0) - 0)**2 + (Fnn2(1) - 0)**2 + (Fnn2(0) - 0)**2 + (Fnn2(1) - 1)**2
= w0**2 + (w2 + w0)**2 + w0**2 + (w2 + w0 - 1)**2
'''

from sympy import diff, lambdify, symbols, pprint

def gradientDescent():
    pass

def lostFn1(a0, a1, a2, h, iterations):
    w1, w2, w0 = symbols('w1 w2 w0')
    Lw1 = w0**2 + w0**2 + (w1 + w0)**2 + (w1 + w0 - 1)**2
    Lw2 = w0**2 + (w2 + w0)**2 + w0**2 + (w2 + w0 - 1)**2

    d1w0 = diff(Lw1, w0)
    d1w1 = diff(Lw1, w1)
    d2w0 = diff(Lw2, w0)
    d2w2 = diff(Lw2, w2)

    pprint(d1w0)
    pprint(d1w1)
    pprint(d2w0)
    pprint(d2w2)

    l1w0 = lambdify([w0, w1], d1w0)
    l1w1 = lambdify([w0, w1], d1w1)
    l2w0 = lambdify([w0, w2], d2w0)
    l2w2 = lambdify([w0, w2], d2w2)

    for i in range(iterations):
        if i%2 == 0:
            _a0 = a0 - h * l1w0(a0, a1)
            _a1 = a1 - h * l1w1(a0, a1)
            a0, a1 = _a0, _a1
        else:
            _a0 = a0 - h * l2w0(a0, a2)
            _a2 = a2 - h * l2w2(a0, a2)
            a0, a2 = _a0, _a2

        print(
            'step', i+1,
            'a0', round(a0, 2),
            'a1', round(a1, 2),
            'a2', round(a2, 2),
        )

def main():
    lostFn1(0, 0, 0, 0.1, 5)

if __name__ == '__main__':
    main()

