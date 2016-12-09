from solution.analysis import *
from equations.resolving_methods import *

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

        base_function = input("f(x)=") #'x**3 - 3*x + 7' #
        derivative = input("f'(x)=") #'3*x**2 - 3' #
        sqr_derivative = input("f''(x)=") #'6*x' #

        print('\n{}'.format('-'*50))  # Исключительно красоты ради

        a, b = input('Введите границы для поиска корня в виде "a, b": ').split(', ')
        print('{}'.format('-'*50))  # Исключительно красоты ради
        range = [float(a), float(b)]

        # Проверить, включен ли режим отладки
        if not self.debug:
            # Предложить включить режим отладки
            if self.__check_choise(self.__make_choise('Желаете выводить промежуточные вычесления?')):
                self.debug = True
        print('{}'.format('-'*50))  # Исключительно красоты ради

        # Предложить использовать точность не по умолчанию
        if self.__check_choise(self.__make_choise('Желаете отказаться от использования точности по умолчанию (0.00001)?')):
            error = float(input('Введите новое значение точности: '))
        else:
            error = 0.00001
        
        methods = [bisection(range, base_function, derivative, sqr_derivative, error, self.debug),  # Метод половинного деления
                   chord(range, base_function, derivative, sqr_derivative, error, self.debug),  # Метод хорд
                   shearing(range, base_function, derivative, sqr_derivative, error, self.debug),  # Метод касательных
                   combo(range, base_function, derivative, sqr_derivative, error, self.debug),  # Комбинированный метод
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