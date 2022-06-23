'''
Следующая таблица содержит информацию об оценках, выставленных фильмам.

Требуется оценить, какую оценку поставит Саша фильму «Гарри Поттер». Сделаем это с помощью метрики Манхэттен (для простоты вычислений данные в таблице нормировать не нужно). Для этого подсчитаем расстояния от Саши до других людей, используя информацию из первых 3 столбцов. Чему равна ожидаемая оценка для «Гарри Поттера» (округлить до одного знака после запятой)?
'''

users = [
    'Vasya',
    'Petya',
    'Masha',
    'Sasha',
]

movies = [
    'The Silence of the Lambs',
    'Titanic',
    'Matrix',
    'Harry Potter',
]

rating = {
    'Vasya': {
        'The Silence of the Lambs': 5,
        'Titanic': 5,
        'Matrix': 5,
        'Harry Potter': 3,
    },
    'Petya': {
        'The Silence of the Lambs': 5,
        'Titanic': 3,
        'Matrix': 4,
        'Harry Potter': 4,
    },
    'Masha': {
        'The Silence of the Lambs': 2,
        'Titanic': 5,
        'Matrix': 3,
        'Harry Potter': 5,
    },
    'Sasha': {
        'The Silence of the Lambs': 3,
        'Titanic': 4,
        'Matrix': 4,
        'Harry Potter': None,
    },
}

def predict():
    uList = ('Vasya','Petya', 'Masha')
    metrics = {
        'Vasya': 0,
        'Petya': 0,
        'Masha': 0,
    }
    for user in uList:
        manhattan = 0
        for movie in ('The Silence of the Lambs', 'Titanic', 'Matrix'):
            manhattan += abs(rating['Sasha'][movie] - rating[user][movie])
        metrics[user] = manhattan

    p1 = 0
    for user in uList:
        p1 += 1 / metrics[user]
    p1 = 1 / p1

    p2 = 0
    for user in uList:
        p2 += rating[user]['Harry Potter'] / metrics[user]

    return round(p1 * p2, 1)

def main():
    p = predict()
    print('p', p)

if __name__ == '__main__':
    main()
