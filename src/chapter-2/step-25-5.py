'''
Следующая таблица содержит информацию об оценках, выставленных фильмам.

Требуется оценить, какую оценку поставит Саша фильму «Гарри Поттер». Сделаем это с помощью метрики Манхэттен (для простоты вычислений данные в таблице нормировать не нужно). Для этого подсчитаем расстояния от Саши до других людей, используя информацию из первых 3 столбцов. Чему равна ожидаемая оценка для «Гарри Поттера» (округлить до одного знака после запятой)?
'''

movies = [
	{
		'name': 'The Silence of the Lambs',
		'scores': { 'Vasia': 5, 'Petia': 5, 'Masha': 2, 'Sasha': 3, }
	},
	{
		'name': 'Titanic',
		'scores': { 'Vasia': 5, 'Petia': 3, 'Masha': 5, 'Sasha': 4, }
	},
	{
		'name': 'Matrix',
		'scores': { 'Vasia': 5, 'Petia': 4, 'Masha': 3, 'Sasha': 4, }
	},
	{
		'name': 'Harry Potter',
		'scores': { 'Vasia': 3, 'Petia': 4, 'Masha': 5, 'Sasha': -1, }
	},
]



def main():
	metrics = []

	for name in ['Vasia', 'Petia', 'Masha']:
		metric = 0
		for i in range(3):
			movie = movies[i]
			metric += abs(movie['scores'][name] - movie['scores']['Sasha'])
		metrics.append(metric)

	print('metrics', metrics)

	left = 1 / (1 / metrics[0] + 1/metrics[1] + 1/metrics[2])
	right = movies[3]['scores']['Vasia'] / metrics[0] + movies[3]['scores']['Petia'] / metrics[1] + movies[3]['scores']['Masha'] / metrics[2]

	print(left * right)

if __name__ == '__main__':
    main()
