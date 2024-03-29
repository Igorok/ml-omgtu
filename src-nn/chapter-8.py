'''
Пример многослойной сети
Fnn (x1, x2) = f(w13 * f(x1 * w11 + x2 * w21 + w01) + w23 * f(x1 * w12 + x2 * w22 + w02) + w03)

Дропаут будем постигать на следующей нейросети:
Fnn(x) = 1 * (x * w1 + w01) + 1 * (x * w2 + w02) + 0 = (x * w1 + w01) + (x * w2 + w02)

В этой сети часть весов уже натренирована и не подлежит изменению в процессе градиентного спуска.
Тренировочная выборка такая:
x   y
0   1
1   2
2   3

Lw = (Fnn(0) - 1)**2 + (Fnn(1) - 2)**2 + (Fnn(2) - 3)**2
Lw = (w01 + w02 - 1)**2 + (w1 + w01 + w2 + w02 - 2)**2 + (2*w1 + w01 + 2*w2 + w02 - 3)**2

Lw1 = (w01 - 1)**2 + (w1 + w01 - 2)**2 + (2*w1 + w01 - 3)**2
Lw1 = (w02 - 1)**2 + (w2 + w02 - 2)**2 + (2*w2 + w02 - 3)**2

Начальные значения всех весов равны 0. Для человека очевидно, что искомая зависимость здесь Y=X+1.
Допустим, что на первой итерации был уничтожен верхний нейрон. Чему равен вес w2 после одного шага градиентного спуска? Шаг спуска h=0.1

'''
from sympy import diff, lambdify, symbols, pprint

def lostFn1(a0, a1, h, iterations):
    w1, w01, w2, w02 = symbols('w1 w01 w2 w02')
    Lw1 = (w01 - 1)**2 + (w1 + w01 - 2)**2 + (2*w1 + w01 - 3)**2
    Lw2 = (w02 - 1)**2 + (w2 + w02 - 2)**2 + (2*w2 + w02 - 3)**2

    dw1 = diff(Lw1, w1)
    dw01 = diff(Lw1, w01)
    dw2 = diff(Lw2, w2)
    dw02 = diff(Lw2, w02)

    pprint(dw1)
    pprint(dw01)
    pprint(dw2)
    pprint(dw02)

    lw2 = lambdify([w2, w02], dw2)
    lw02 = lambdify([w2, w02], dw02)

    for i in range(iterations):
        _a0 = a0 - h * lw2(a0, a1)
        _a1 = a1 - h * lw02(a0, a1)
        a0, a1 = _a0, _a1
        print(
            'step', i+1,
            'a0', round(a0, 2),
            'a1', round(a1, 2),
        )

def main():
    lostFn1(0, 0, 0.1, 3)

if __name__ == '__main__':
    main()
