from solution.analysis import *
from integrals.resolving_methods import *

class solution:

    def __init__(self, analyze=False, debug=False):
        '''Инициализировать объект класса'''
        self.debug = debug
        self.analyze = analyze

    def __check_choise(self, choise):
        '''Обработать выбор пользователя'''
        choise = choise.lower()
        if choise == 'y' or choise == 'yes':
            return True
        elif choise == 'n' or choise == 'no':
            return False
        else:
            return None

    def __make_choise(self, title):
        '''Предоставить пользователю выбор.'''

        return input('{}(y/n): '.format(title))

    def run(self):
        '''Выполнить программу.'''

        print('{}\n'.format('-'*50))  # Исключительно красоты ради

        base_function = input("f(x)=") #'x**2' #

        print('\n{}'.format('-'*50))  # Исключительно красоты ради

        a, b = input('Введите пределы интегрирования(нижний-верхний) в виде "a, b": ').split(', ')
        print('{}'.format('-'*50))  # Исключительно красоты ради
        range = [float(a), float(b)]

        # Проверить, включен ли режим отладки
        if not self.debug:
            # Предложить включить режим отладки
            if self.__check_choise(self.__make_choise('Желаете выводить промежуточные вычесления?')):
                self.debug = True
        print('{}'.format('-'*50))  # Исключительно красоты ради

        # Предложить использовать точность не по умолчанию
        if self.__check_choise(self.__make_choise('Желаете отказаться от использования точности по умолчанию (0.001)?')):
            error = float(input('Введите новое значение точности: '))
        else:
            error = 0.001
        
        methods = [left_rect(range, base_function, error, self.debug),  # Метод левых прямоугольников
                   right_rect(range, base_function, error, self.debug),  # Метод правых прямоугольников
                   middle_rect(range, base_function, error, self.debug),  # Метод средних прямоугольников
                   trapeze(range, base_function, error, self.debug),  # Метод трапеций
                   parabole(range, base_function, error, self.debug),  # Метод трапеций
                   ]

        # Просто решить уравнения
        
        print('{}\n'.format('-'*50))  # Исключительно красоты ради
        for n, i in enumerate(methods):
            print('{}. {}'.format(n + 1, i.resolve()))
        
        print('\n{}'.format('-'*50))  # Исключительно красоты ради

        if self.analyze:
            # Провести анализ
            if self.__check_choise(self.__make_choise('Желаете изменить параметры анализа по умолчанию (мин, макс точность, шаг)?')):
                
                min_error = float(input('Введите новое значение минимальной точности: '))
                max_error = float(input('Введите новое значение максимальной точности: '))
                error_step = float(input('Введите новое значение шаг изменения точности: '))

                _analyzer = analyzer(methods, min_error, max_error, error_step)
            else:
                _analyzer = analyzer(methods)

            _analyzer.run()