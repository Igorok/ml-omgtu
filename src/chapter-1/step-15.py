'''
Однажды я попросил, чтобы студенты ответили на два вопроса анкеты «ваш год рождения» и «ваш возраст».
Из их ответов я сформировал таблицу, в которой был столбец Р=«год рождения студента» и Q=«возраст студента».
Оказывается, значение коэффициента корреляции признаков P и Q зависит от месяца, в котором проводилось анкетирование (это не шутка!). Укажите два месяца, которым соответствует наименьшее (по модулю) значение коэффициента корреляции признаков P и Q.
'''

import datetime
import random
from dateutil.relativedelta import relativedelta
import pandas as pd

class StudentCorrelationGenerator:
    def __init__(self):
        self.students = [
            datetime.date(
                2000 + random.randint(1, 3),
                random.randint(1, 12),
                random.randint(1, 28)
            ) for _ in range(100)
        ]

    def generate(self):
        for month in range(1, 13):
            today = datetime.date(datetime.date.today().year, month, 1)
            studentsAge = []
            for birthday in self.students:
                difference = relativedelta(today, birthday).years
                studentsAge.append((birthday.year, difference))

            df = pd.DataFrame(studentsAge, columns=['Year', 'Age'])
            corr = df.corr(method='pearson')
            print(today.strftime('%B'), corr['Year']['Age'])

def main():
    corGenerator = StudentCorrelationGenerator()
    corGenerator.generate()

if __name__ == '__main__':
    main()

'''
January -0.9999999999999915
February -0.9368164269528866
March -0.9172923686569986
April -0.874675360330634
May -0.856384589548095
June -0.8564937301321808
July -0.8505264421658885
August -0.8553852835844752
September -0.8644254815611195
October -0.8877873666865913
November -0.9167287531971757
December -0.9523219780412474

January -1.0000000000000029
February -0.9455716305376343
March -0.8944442386411174
April -0.8660680874145249
May -0.8567742644799615
June -0.8513103269755093
July -0.8549524318289469
August -0.8523138637373815
September -0.8673497147007846
October -0.8764092640170438
November -0.9080962284148066
December -0.9498732309521019

January -0.9999999999999925
February -0.9495410215076745
March -0.9210972802606919
April -0.8868688128515262
May -0.8690931939003599
June -0.8666072051484714
July -0.8672707589944649
August -0.8677242613766528
September -0.8780109940529784
October -0.8771449499875996
November -0.8980368126924313
December -0.9573983835818997
'''
