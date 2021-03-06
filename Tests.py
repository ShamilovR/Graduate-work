from random import choice

class Test:
    def __init__(self):
        self.question1 = {'Метод покоординатного спуска заключается в: ': [
            {'в изменении каждый раз одной переменной': False},
            {'все, кроме одной переменной остаются постоянными': False},
            {'оба варианта ответа верны': False},
            {'оба варианта ответа не верны ': True}]}

        self.question2 = {'Метод покоординатного спуска является: ': [
            {'простым в реализации, но скорость сходимости невысокая': True},
            {'простым в реализации, но скорость сходимости высокая': False},
            {'реализация трудна, скорость сходимости высокая': False},
            {'реализация трудна, скорость сходимости невысока ': False}]}

        self.question3 = {'Какой метод является более модифицированной версией покоординатного спуска?': [
            {'поиск по правильному симплексу': False},
            {'метод Зейделя': True},
            {'поиск по деформируемому многограннику': False},
            {'метод золотого сечения': False}]}

        self.question4 = {'Что происходит с переменными в методах покоординатного спуска простейшего типа?': [
            {'меняется одна переменная': True},
            {'меняются две переменные': False},
            {'меняются три переменные': False},
            {'меняются все переменные': False}]}

        self.question5 = {'Если за один цикл из n этапов при переборе направлений всех координатных векторов e^1,…,e^n с шагом a_k не реализовалось ни одного удачного этапа, что происходит с шагом?': [
            {'остается прежним': False},
            {'увеличивается в два раза': False},
            {'уменьшается на 0,1 раз': False},
            {'дробится': True}
        ]}

        self.question6 = {'В каком случае длина шага a_k не дробится?': [
            {'если реализовался хотя бы один удачный этап': True},
            {'если реализовалось два удачных этапа': False},
            {'если не реализовался ни один удачный этап': False},
            {'Ничего из вышеперечисленного': False}
        ]}

        self.question7 = {'Методы покоординатного спуска простейшего типа заключаются в': [
            {'изменении каждый раз каждой переменной': False},
            {'изменении каждый раз одной переменной, тогда как другие остаются постоянными': True},
            {'изменении каждый раз двух переменных, тогда как другие остаются постоянными': False},
            {'ничего из вышеперечисленного': False}
        ]}

        self.question8 = {'Методы покоординатного спуска работают плохо, когда': [
            {'если в выражение минимизируемой функции входят произведения x_i*x_j': True},
            {'если в выражение минимизируемой функции входят суммы x_i и x_j': False},
            {'если в выражение минимизируемой функции входят разности x_i и x_j': False},
            {'если в выражение минимизируемой функции входят квадраты x_i и x_j': False}
        ]}

        self.question9 = {'Методы покоординатного спуска простейшего типа заключаются в изменении каждый раз одной переменной, тогда как другие:': [
            {'остаются постоянными': True},
            {'рандомно меняются': False},
            {'равны нулю': False},
            {'нет правильного ответа': False}
        ]}

        self.question10 = {'Метод покоординатного спуска широко применяется на практике благодаря': [
            {'наилучшей точности': False},
            {'быстрой сходимости': False},
            {'простоте реализации': True},
            {'нет правильного ответа': False}
        ]}

        self.question11 = {'Следующая модификация метода покоординатного спуска, известна под названием': [
            {'метод Ньютона': False},
            {'метод Зейделя': True},
            {'метод дихотомии': False},
            {'метод перебора': False}
        ]}

        self.question12 = {'Метод Зейделя является улучшенной модификацией другого метода. Какого?': [
            {'метода поиска по деформируемому многограннику': False},
            {'метода циклического покоординатного спуска': True},
            {'метода градиентного спуска': False},
            {'метода наискорейшего спуска': False}
        ]}

        self.question13 = {'С какой точки начинается последовательная минимизация f(X) по направлению каждого из координатных векторов e^j,j=1,…,n?': [
            {'с самой первой точки построенной последовательности': False},
            {'с самой последней точки построенной последовательности': True},
            {'с самого центра тяжести построенной последовательности': False},
            {'с симметричной точки от точки минимума': False}
        ]}

        self.question14 = {'Основной цикл метода Зейделя называется': [
            {'внешней итерацией': True},
            {'внутренней итерацией': False},
            {'последовательной итерацией': False},
            {'ни один из вышеперечисленных': False}
        ]}

        self.question15 = {'Суть метода Зейделя заключается в том, чтобы на каждой итерации по очереди ': [
            {'минимизировать функцию перпендикулярно каждой из координат': False},
            {'минимизировать функцию вдоль каждой из координат': False},
            {'усреднить значения функции вдоль каждой из координат': False},
            {'минимизировать функцию вдоль каждой из координат': True}
        ]}

        self.question16 = {'Минимум функции удастся найти с помощью метода Зейделя за конечное число шагов, если линиями уровня целевой функции двух переменных являются': [
            {'концентрические окружности': True},
            {'параболы': False},
            {'гиперболы': False},
            {'синусоида': False}
        ]}

        self.question17 = {'Отличие от метода Зейделя от метода покоординатного спуска-поиск по каждой из координат x_i, i = 1,..,n осуществляется:': [
            {'с некоторым «наилучшим» шагом, который обеспечивает так называемый исчерпывающий спуск.': True},
            {'с некоторым «случайным» шагом, который обеспечивает так называемый исчерпывающий спуск.': False},
            {'с некоторым «худшим» шагом, который обеспечивает так называемый исчерпывающий спуск.': False},
            {'не с произвольно выбранным шагом a (который впоследствии может уменьшаться), а с некоторым «наилучшим» шагом, который не может  обеспечить так называемый исчерпывающий спуск.': False}
        ]}

        self.question18 = {'Как влияет на количество итераций уменьшение значений a и λ': [
            {'количество итераций увеличивается': True},
            {'количество итераций уменьшается': False},
            {'изменений нет': False},
            {'влияет незначительно': False}
        ]}

        self.question19 = {'Какие параметры нужно задать при градиентном спуске?': [
            {'Начальной точки': False},
            {'Скорости уменьшения шага': False},
            {'Начальной точки, скорости уменьшения шага, параметр точности': True},
            {'Начальный шаг и параметр точности': False}
        ]}

        self.question20 = {'К группе каких методов относится метод градиентного спуска?': [
            {'покоординатного спуска': False},
            {'безусловной минимизации, использующие производные': True},
            {'в задачах одномерной оптимизации': False},
            {'безусловного спуска': False}
        ]}

        self.question21 = {'Сколько шагов представлено в общем алгоритме метода градиентного спуска': [
            {'8': False},
            {'4': False},
            {'3': False},
            {'5': True}
        ]}

        self.question22 = {'К методам безусловной оптимизации относятся': [
            {'метод равномерного поиска': False},
            {'метод градиентного спуска': True},
            {'метод золотого сечения': False},
            {'метод дихотомии': False}
        ]}

        self.question23 = {'Если процедура градиентного спуска сходится медленно, это означает, что': [
            {'сильное изменение некоторых переменных приводит к резкому изменению значения функции': False},
            {'сильное изменение некоторых переменных приводит к незначительному изменению значения функции': False},
            {'малое изменение некоторых переменных приводит к резкому изменению значения функции': True},
            {'малое изменение некоторых переменных приводит к незначительному изменению значения функции': False}
        ]}

        self.question24 = {'К группе каких методов относится метод наискорейшего спуска?': [
            {'методам безусловной минимизации, использующие производные': True},
            {'методам покоординатного спуска': False},
            {'методам в задачах одномерной оптимизации': False},
            {'методам безусловного спуска': False}
        ]}

        self.question25 = {'В чем отличие метода наискорейшего спуска от метода градиентного спуска?': [
            {'используется направление градиента': False},
            {'используется направление антиградиента': False},
            {'используется решение вспомогательной задачи одномерной оптимизации': True},
            {'используется решение дополнительной задачи с помощью метода циклического покоординатного спуска': False}
        ]}

        self.question26 = {'Вектор, своим направлением показывающий направление наискорейшего возрастания некоторой величины': [
            {'градиент': True},
            {'антиградиент': False},
            {'симплекс': False},
            {'опорный вектор': False}
        ]}

        self.question27 = {'Величина шага находится в результате решения вспомогательной задачи': [
            {'одномерной минимизации': True},
            {'многомерной минимизации': False},
            {'безусловной оптимизации': False},
            {'условной оптимизации': False}
        ]}

        self.question27 = {'На каждой итерации в направлении антиградиента выполняется ______ спуск': [
            {'вероятностный': False},
            {'исчерпывающий': True},
            {'полный': False},
            {'быстрый': False}
        ]}

        self.question28 = {'В методе наискорейшего спуска исчерпывающий спуск выполняется направлении': [
            {'градиента': False},
            {'антиградиента': True},
            {'верно все': False},
            {'нет правильного ответа': False}
        ]}

        self.question29 = {'Метод наискорейшего спуска основывается': [
            {'на методе Зейделя': False},
            {'на методе дихотомии': False},
            {'на методе перебора': False},
            {'на методе градиентного спуска': True}
        ]}

        self.question30 = {'Когда применяются алгоритмы случайного поиска?': [
            {'невозможно определить градиент': True},
            {'велика размерность задачи': False},
            {'невозможно решить методом штрафных функций': False},
            {'все вышеперечисленное': False}
        ]}

        self.question31 = {'Модификацией какого метода является алгоритм с возвратом при неудачном шаге': [
            {'метод дихотомии': False},
            {'метод случайного поиска': True},
            {'метод золотого сечения': False},
            {'метод Зейделя': False}
        ]}

        self.question32 = {'Влияет ли выбор параметров алгоритма на его эффективность, если да то насколько': [
            {'да, но не оказывает существенного влияния': False},
            {'да, существенно': True},
            {'нет': False},
            {'ни один из вышеперечисленных ответов': False}
        ]}

        self.question33 = {'Простейшей реализацией метода случайного поиска считается:': [
            {'метод перебора': False},
            {'алгоритм с возвратом при неудачном шаге': True},
            {'алгоритм наилучшей пробы': False},
            {'метод наискорейшего спуска': False}
        ]}

        self.question34 = {'К методам случайного поиска относится:': [
            {'метод перебора': False},
            {'метод Зейделя': False},
            {'алгоритм наилучшей пробы': True},
            {'метод наискорейшего спуска': False}
        ]}

        self.question35 = {'Если все точки оказываются вне области R, то пробы повторяются': [
            {'с уменьшенным значением a': True},
            {'с увеличенным значением a': False},
            {'Без значения a': False},
            {'Нет правильного ответа': False}
        ]}

        self.question36 = {'Откуда берется некоторое заданное количество реализаций случайного вектора?': [
            {'датчик случайных чисел': True},
            {'детерминированный набор чисел': False},
            {'все точки, принадлежащие области R': False},
            {'ни один из вышеперечисленных вариантов': False}
        ]}

        self.question37 = {'В качестве очередного (k+1)-го приближения выбирается пробная точка, в которой значение функции оказалось': [
            {'наименьшим': True},
            {'наибольшим': False},
            {'случайным': False},
            {'ни один из вышеперечисленных': False}
        ]}

        self.question38 = {'Выбором каких параметров данного алгоритма можно улучшить его сходимость?': [
            {'a>0': False},
            {'s>1 и a>0': True},
            {'s>1': False},
            {'b>0': False}
        ]}

        self.question39 = {'Если все эти точки оказываются вне области, то': [
            {'Пробы повторяются с увеличенным значением a': False},
            {'Пробы повторяются с уменьшенным значением a': True},
            {'Пробы повторяются с неизменным значением a': False},
            {'Нет правильного ответа': False}
        ]}

        self.question40 = {'Откуда берется некоторое заданное количество реализаций случайного вектора?': [
            {'все точки, принадлежащие области r': False},
            {'детерминированный набор чисел': False},
            {'датчик случайных чисел': True},
            {'ни один из вышеперечисленных вариантов': False}
        ]}

        self.question41 = {'Построенный вектор P^k в алгоритме называют': [
            {'статическим антиградиентом': False},
            {'нулевым градиентом': False},
            {'статическим градиентом': True},
            {'нулевым антиградиентом': False}
        ]}

        self.question42 = {'Выбором каких параметров данного алгоритма можно улучшить его сходимость?': [
            {'s>1, b>0': False},
            {'s>1, a>0': False},
            {'s>1, a>0, b>0': True},
            {'a>0, b>0': False}
        ]}
        self.questions = [self.question1, self.question2, self.question3, self.question4, self.question5, self.question6,
                          self.question7, self.question8, self.question9, self.question10, self.question11, self.question12,
                          self.question13, self.question14, self.question15, self.question16, self.question17, self.question18,
                          self.question19, self.question20, self.question21, self.question22, self.question23, self.question24,
                          self.question25, self.question26, self.question27, self.question28, self.question29, self.question30,
                          self.question31, self.question32, self.question33, self.question34, self.question35, self.question36,
                          self.question37, self.question38, self.question39, self.question40, self.question41, self.question42]

    def random_question(self):
        random_questions = []
        while len(random_questions) != len(self.questions):
            new_question = choice(self.questions)
            if new_question not in random_questions:
                random_questions.append(new_question)

        return random_questions
