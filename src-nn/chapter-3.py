'''
Задача на применение формулы про дифференцирование сложной функции (см. слайд, где была картина Э. Мунка «Крик»). Пусть f(g1,g2,g3)=g1*g2*g3; g1=x2+x3; g2=x1+x3; g3=x1+x2. Найдите частные производные сложной функции f(g1,g2,g3) по переменным x1,x2,x3. Не забудьте потом вхождения букв g1,g2,g3 заменить на их выражения через буквы x1,x2,x3. А в ответ напишите значение f'( x3)(1,2,3).

f'(x1) = f'(g1)*g1'(x1) + f'(g2)*g2'(x1) + f'(g3)*g3'(x1)
f'(x2) = f'(g1)*g1'(x2) + f'(g2)*g2'(x2) + f'(g3)*g3'(x2)
f'(x3) = f'(g1)*g1'(x3) + f'(g2)*g2'(x3) + f'(g3)*g3'(x3)

f'(g1) = g2*g3
f'(g2) = g1*g3
f'(g3) = g1*g2

g1'(x3) = 1
g2'(x3) = 1
g1'(x3) = 0

f'(x3) = g2*g3+g1*g3 = g3(g2+g1) = (x1+x2)*(x1+x3+x2+x3) = 3*9=27
'''

'''
Можете построить граф вычислений, если я укажу последовательность операций, которые применяются к переменным (ибо рисовать готовую картинку – лень).
Итак, у нас будет одна переменная х (это будет единственный лист графа). Далее идут вершины a:=2^x; b:=3^x; c:=a+b; d:=ab; f:=c/d, где f - корень графа (он соответствует всей функции f(x)).
Последовательно найдите частные производные ∂f/∂c, ∂f/∂d, ∂f/∂a, ∂f/∂b, ∂f/∂x. Собственно, последняя частная производная в списке и будет окончательным ответом.
В окошко ответа запишите значение ∂f/∂x(1).

P.S. Свои вычисления можно проверить "в лоб". Очевидно, что можно раскрутить выражение для f и получить выражение для f через букву x. Должно получиться f(x)=(2^x+3^x)/6^x (понятно, откуда шестёрка появилась?). После этого выражение можно продифференцировать по школьным правилам, подставить x=1 и получить ответ.

f = c/d
с = a+b
d = a*b
b = 3^x
a = 2^x

f'x = ?
f'c = 1/d
f'd = -c/d^2
c'a = 1
c'b = 1
d'a = b
d'b = a
b'x = 3^x*ln3
a'x = 2^x*ln2

f'x = f'c*c'x + f'd*d'x
= 1/d * (c'a*a'x + c'b*b'x) - 1/d^2 * (d'a*a'x + d'b*b'x)
= 1/d * (1*2^x*ln2 + 1*3^x*ln3) - c/d^2 * (b*2^x*ln2 + a*3^x*ln3)
= (2^x * ln2 + 3^x * ln3)/(a*b) - (a+b)(3^x * 2^x * ln2 + 2^x * 3^x * ln3)/(a*b)^2
= (2^x * ln2 + 3^x*ln3)/6^x - (2^x+3^x)(6^x * ln2 + 6^x * ln3)/6^2x
= (12^x*ln2 + 18^x*ln3 - 12^x*ln2 - 12^x*ln3 - 18^x*ln2 - 18^x*ln3) / 6^2x
= -(12^x*ln3 + 18^x*ln2)/6^2x
= -(12ln3 + 18ln2) / 36
= -(2ln3 + 3ln2)/6 = -(2.20 + 2.08)/6 = 0.71
'''

'''
Можете построить граф вычислений, если я укажу последовательность операций, которые применяются к переменным (ибо рисовать готовую картинку – лень).
Итак, у нас будет теперь две переменных x1, x2 (значит, в графе будет 2 листа). Далее идут вершины a:=x1*x2; b:=x1+x2; c:=a*b; d:=a+b; f:=c^2+d^2, где f - корень графа (он соответствует всей функции f(x1, x2)).
Последовательно найдите частные производные ∂f/∂c, ∂f/∂d, ∂f/∂a, ∂f/∂b, ∂f/∂x1, ∂f/∂x2. Собственно, последние две частных производных в списке и будут окончательным ответом.
В окошко ответа запишите значение ∂f/∂x1 (1,1).

P.S. Свои вычисления можно проверить "в лоб". Очевидно, что можно раскрутить выражение для f и получить выражение для f через буквы x1,x2. Должно получиться f(x1,x2)=(x1^2*x2 + x1*x2^2)^2 + (x1x2 + x1 + x2)^2. После этого выражение можно продифференцировать по школьным правилам, подставить x1=1, x2=1 и получить ответ.

a = x1 * x2
b = x1 + x2
c = a * b
d = a + b
f = c^2 + d^2

f'(x1) (1,1)
f'c = 2c
f'd = 2d
c'a = b
c'b = a
d'a = 1
d'b = 1
a'x1 = x2
b'x1 = 1

f'x1 = f'c*c'x1 + f'd*d'x1 = 2c*(c'a*a'x1 + c'b*b'x1) + 2d*(d'a*a'x1 + d'b*b'x1) =
2c*(b*x2 + a*1) + 2d*(1*x2 + 1*1) = 2c*(b*x2 + a) + 2d*(x2 + 1) =
2*a*b*((x1+x2)*x2 + x1*x2) + 2(a+b)*(x2+1) = 2*x1*x2*(x1+x2)*((x1+x2)*x2 + x1*x2) + 2*(x1*x2+x1+x2)*(x2+1) =
2*1*1*2*(2*1+1) + 2*(1+2)*2 = 12 + 12 = 24
'''

'''
Теперь мы можем воспользоваться определением сигмоиды sigma(x)=e^x/(e^x+1) и оценить производные в точке x=0. Получаем:
sigma'(0) < sigma(0)=0.5
(sigma(sigma(0)))' < sigma(sigma(0)) * sigma(0) = 0.62 * 0.5 = 0.31
Напишите, какое число получается в неравенстве для производной (sigma(sigma(sigma(x))))'.

(sigma(sigma(sigma(x))))' = sigma(sigma(sigma(x))) * sigma(sigma(x)) * sigma(x)

e^0 / (e^0 + 1) = 0.5
e^0.5 / (e^(0.5) + 1) = 1.65 / (1.65 + 1) = 0.62
e^0.62 / (e^0.62 + 1) = 1.86 / (1.86 + 1) = 0.65
0.65 * 0.62 * 0.5 = 0.20




























'''
