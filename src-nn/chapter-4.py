'''
Relu(x1*w11 + x2*w12 + w10)

Теперь представьте себе такой искусственный нейрон: ему на вход подается число x, затем оно домножается на вес связи w1, внутри нейрона прибавляется вес-смещение w0 и после этого применяется функция активации сигмоида σ.
Нарисуйте схему такого нейрона (я бы сам это сделал, но лень, и таланта к рисованию нет )))).
Допустим, что в наш нейрон подали вход x=1 и получили ответ 0.5, потом подали вход x=2 и снова получили ответ 0.5.
Чему равны веса w0, w1? В окошко ответа напишите значение w1.

sigma = e^x / (1 + e^x)
x = 0
sigma = 1 / (1 + 1) = 0.5

x*w1 + w0 = 0

2*w1 + w0 = w1 + w0
w1 = 0
'''

'''
Теперь представьте себе такой искусственный нейрон: у него два входа x1, x2, и эти входы нейрон преобразует в значение F(x1, x2) = w1*x1 + x2*w2 + w0.
Нарисуйте схему такого нейрона. Как видно, у него вообще нет функции активации.
В наш нейрон поступают не одиночные числа, а пары чисел (x1, x2). Допустим, что наш нейрон выдал  следующие ответы: F(1,0)=4; F(0,1)=5; F(1,1)=6. Чему равны веса w0, w1, w2?
В окошко ответа напишите значение w0

w1 + w0 = 4
w2 + w0 = 5
w1 + w2 + w0 = 6

x1 = 4 - w0
x2 = 5 - w0

4 - w0 + 5 - w0 + w0 = 6
9 - w0 = 6
w0 = 3
'''

'''
Представьте себе такую многослойную нейронную сеть: у нее входной слой размерности 4, далее идут внутренние полносвязные слои, состоящие соответственно из 10, 20, 5 нейронов. Вся сеть заканчивается выходным слоем из одного нейрона.
Сколько в этой сети весов-связей и весов-смещений? Напишите в ответ общее количество весов всех типов.

4
10
20
5
1

смещение - 36
свзи - 4*10 + 10*20 + 20*5 +5*1 = 345
345 + 36 = 381
'''

'''
Представьте себе такую многослойную нейронную сеть:
- у нее входной слой размерности 1;
- далее идут два внутренних полносвязных слоя с неизвестным числом нейронов, причем количество нейронов на первом внутреннем слое больше числа нейронов на втором внутреннем слое;
- вся сеть заканчивается выходным слоем из одного нейрона.
Известно, что во всей сети число весов-смещений равно 10, а весов-связей 29.
Найдите, чему равно  количество нейронов на втором внутреннем слое, и запишите это в окошко ответа.

1
x
y
1

x > y
x + y + 1 = 10
x + x*y + y = 29

x = 9 - y
9 - y + 9y - y^2 + y = 29
9y - y^2 = 20
-y^2 + 9y - 20 = 0
y^2 - 9y + 20 = 0

D = b^2 - 4ac. А вот свойства дискриминанта:
если D < 0, корней нет;
если D = 0, есть один корень;
если D > 0, есть два различных корня.

D = 81 - 80 = 1
x = (-b +- D^(1/2)) / 2*a

(9 +- 1) / 2 = 4
y = 4
x = 5

5 + 20 + 4 = 29
'''

'''
Ниже приведена нейросеть с известными значениями весов. Все функции активации - это Relu. Чему равен выход нейросети, если х=2?

f1 = relu(x*w10 + w11) * w12
f2 = relu(x*w20 + w21) * w22
f = relu(f1 + f2 + w3)

f1 = relu(2*1 + 1) * (-2) = -6
f2 = relu(2*2 - 5) * 4 = 0 // relu выдала 0, цепочка дальше не пойдет
f = -6 + 10 = 4
'''

'''
Возьмем нейросеть из прошлой задачи. Чему может быть равен x, если известно, что нейросеть выдала ответ 12?

f1 = relu(x*w10 + w11) * w12
f2 = relu(x*w20 + w21) * w22
f = relu(f1 + f2 + w3)

f1 = relu(x + 1) * (-2)
f2 = relu(2x - 5) * 4
relu(relu(x + 1) * (-2) + relu(2x - 5) * 4 + 10) = 12
relu(x + 1) * (-2) + relu(2x - 5) * 4 + 10 = 12
relu(x + 1) * (-2) + relu(2x - 5) * 4 = 2
4 * relu(2x - 5) - 2 * relu(x + 1) = 2
4x - 10 - x - 1 = 1
3x = 12
x = 4

f1 = -10
f2 = 12
f = -10 + 12 + 10 = 12
'''





