'''
На видео долго и нудно говорилось, что при подаче данных на вход нейросети их нужно нормализовать. Вот вам табличка с данными, которую мы будем мучить несколько шагов. У нее 3 нецелевых признака, которые нужно нормализировать.

Пациент     Вес     Пол     Группа крови    Y-здоров
A1          50      0       1               0
A2          60      1       2               1
A3          80      1       3               0
A4          100     0       4               1

Мы будем работать с формулой нормализации
xi = (xi-a)/(b-a)
где a и b - соответственно минимальное и максимальное значение в столбце.
'''

'''
Напишите в окошечко, чему будет равно значение признака "Вес" у третьего объекта после нормализации.
'''

import statistics

def normalise1(arr, newItem=0):
    minVal = min(arr)
    maxVal = max(arr)
    bottom = maxVal-minVal
    return [
        [round((v - minVal) / bottom, 2) for v in arr],
        round((newItem - minVal) / bottom, 2)
    ]

'''
xi = (xi - x_mean) / s
s - величина отклонения в столбце
'''
def normalise2(arr, newItem=0):
    x_mean = statistics.mean(arr)
    s = 0
    for x in arr:
        s += (x - x_mean)**2
    s = round((s / (len(arr)-1)) ** 0.5, 2)

    return [
        [round(((x - x_mean) / s), 2) for x in arr ],
        round(((newItem - x_mean) / s), 2)
    ]

def main():
    normalised = normalise2([50, 60, 80, 100], 90)
    # normalised = normalise2([0, 1, 1, 0], 0)
    print(normalised)

if __name__ == '__main__':
    main()


