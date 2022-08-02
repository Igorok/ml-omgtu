'''
Со школы мы знаем, что чем круче график функции идёт вверх, тем больше значение производной (ибо производная - это скорость изменения функции). Естественно, крутизна графика влияет на ускорение нашего "шарика" из процедуры градиентного спуска. Вот вам теперь функция f(x)=x^4. Представьте себе, что наш "шарик" находится в точке с координатой a[0]=2. Мы запускаем процедуру градиентного спуска из точки a[0] c шагом h=0.1. Найдите позицию шарика на следующем шаге a[1]. Ну как: он прошел бОльшее расстояние, чем в предыдущей задаче (где мы брали функцию f(x)=x^2?
В ответе будет отрицательное число. Это означает, что шарик настолько разогнался, что проскочил точку минимума x=0. Взрыв градиента, однако!

f' = 4x**3
a[0] = 2
a[1] = 2 - 0.1 * (4 * 2**3) = 2 - 0.1 * 32 = 2 - 3.2 = -1.2

a[n+1] = a[n] - h * f'(a[n])

А теперь устроим градиентный спуск по функции f(x)=1/x. Из ее графика понятно, что при больших положительных x у функции имеется плато, на котором градиентный спуск практически останавливается (затухание градиента). Чему равна позиция шарика a[0], если известно, что его следующая позиция a[1] находится на расстоянии всего-то 10^-6 от позиции a[0]. Шаг обучения равен h=0.01.
'''

def derivativeFn2(x):
    return 2 * x

def derivativeFn4(x):
    return 4 * (x**3)

def getPoint(a, h, fn, step):
    i = 0
    while i < step:
        aPrev = a
        a = round(a - h * fn(a), 2)
        i += 1
        print(
            'step', i,
            'a', a,
            'diff', abs(round(a - aPrev, 2))
        )
    return a

'''
a[n+1] = a[n] - h * f'(a[n])

А теперь устроим градиентный спуск по функции f(x)=1/x. Из ее графика понятно, что при больших положительных x у функции имеется плато, на котором градиентный спуск практически останавливается (затухание градиента). Чему равна позиция шарика a[0], если известно, что его следующая позиция a[1] находится на расстоянии всего-то 10^-6 от позиции a[0]. Шаг обучения равен h=0.01.

a[1]-a[0] = 10^-6
(x^-1)' = -1 * x^-2 = -1 * x^-2


a[1] = a[0] - h * f'(a[0])
a[1] - a[0] = - h * f'(a[0])
10^-6 = - 10^-2 * -1 * x^-2
10^-4 = x^-2
1 / 10000 = 1 / x^2
'''

'''
В предыдущем параграфе вы искали минимум и строили график функции   f(x)=x(x^2 - 9). Из графика (при условии, что вы его правильно построили) следует, что "шарик" может скатиться как в точку минимума, так и заняться бесконечным спуском в бездонную пропасть слева. Давайте убедимся в том, что шарик из точки a[0]= -1 будет катиться по направлению к точке минимума (которую вы должны были найти на предыдущем шаге).
Пусть h = 0.1, вычислите позицию шарика a[2] после двух шагов градиентного спуска и запишите ее в ответ. Действительно ли шарик приблизился к точке минимума?

f = x * (x^2 - 9) = x^3 - 9x
f' = 3x^2 - 9
'''
def derivativeFnX29(x):
    return 3 * (x**2) - 9


def main():
    # a22 = getPoint(2, 0.1, derivativeFn2, 2)
    # print('a22', a22)

    # a41 = getPoint(2, 0.1, derivativeFn4, 1)
    # print('a41', a41)

    # print('2')
    # getPoint(0.71, 0.1, derivativeFn2, 10)
    # print('4')
    # getPoint(0.71, 0.1, derivativeFn4, 10)

    getPoint(-2, 0.1, derivativeFnX29, 5)

if __name__ == '__main__':
    main()