# from resolving import resolving
from integrals.resolving import resolving

import copy


class integrals_resolving:
    '''Материнский класс для решения уравнений.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        '''Инициализация.'''
        # if isinstance(base_function, function) and isinstance(derivative, function) and isinstance(sqr_derivative, function):
        self.base_function = base_function
        self.error = error
        self.range = range
        self.method_name = None
        self.debug = debug

    def __str__(self):
        '''Вернуть строковое представление объекта класса.'''
        return self.method_name

    def f(self, x):
        '''Основная функция вида f(x)=...'''
        return eval(self.base_function)

    def resolve(self):
        '''Решить.'''
        if self.debug:
            print('{}, error={}'.format(self.method_name, self.error))


class left_rect(integrals_resolving):
    '''Класс, описывающий логику вычисления интеграла функции методом левых прямоугольников.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Метод левых прямоугольников'

    def resolve(self):
        '''Вычисление интеграла методом левых прямоугольников.'''
        super().resolve()
        a, b = self.range
        n = 0
        s = 0
        s1 = self.error * 10
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x_boof = a
            for i in range(0, split_count):
                x = x_boof + i*h
                s += self.f(x)

            s *= h
            split_count *= 2
            if self.debug:
                print('{0}: {1}'.format(n, s))

        return resolving.from_dict({'steps': n,
                                    'value': s,
                                    'method_name': self.method_name})


class right_rect(integrals_resolving):
    '''Класс, описывающий логику вычисления интеграла функции методом правых прямоугольников.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Метод правых прямоугольников'

    def resolve(self):
        '''Вычисление интеграла методом правых прямоугольников.'''
        super().resolve()
        a, b = self.range
        n = 0
        s = 0
        s1 = self.error * 10
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x_boof = a
            for i in range(1, split_count+1):
                x = x_boof + i*h
                s += self.f(x)

            s *= h
            split_count *= 2
            if self.debug:
                print('{0}: {1}'.format(n, s))

        return resolving.from_dict({'steps': n,
                                    'value': s,
                                    'method_name': self.method_name})


class middle_rect(integrals_resolving):
    '''Класс, описывающий логику вычисления интеграла функции методом средних прямоугольников.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Метод средних прямоугольников'

    def resolve(self):
        '''Вычисление интеграла методом средних прямоугольников.'''
        super().resolve()
        a, b = self.range
        n = 0
        s = 0
        s1 = self.error * 10
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x_boof = copy.deepcopy(a) + h/2
            for i in range(0, split_count):
                x = x_boof + i*h
                s += self.f(x)

            s *= h
            split_count *= 2
            if self.debug:
                print('{0}: {1}'.format(n, s))

        return resolving.from_dict({'steps': n,
                                    'value': s,
                                    'method_name': self.method_name})


class trapeze(integrals_resolving):
    '''Класс, описывающий логику вычисления интеграла функции методом трапеций.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Метод трапеций'

    def resolve(self):
        '''Вычисление интеграла методом трапеций.'''
        super().resolve()
        a, b = self.range
        n = 0
        s = 0
        s1 = self.error * 10
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x_boof = copy.deepcopy(a)
            s = (self.f(a) + self.f(b)) / 2

            for i in range(1, split_count):
                x = x_boof + i*h
                s += self.f(x)

            s *= h
            split_count *= 2
            if self.debug:
                print('{0}: {1}'.format(n, s))

        return resolving.from_dict({'steps': n,
                                    'value': s,
                                    'method_name': self.method_name})


class parabole(integrals_resolving):
    '''Класс, описывающий логику вычисления интеграла функции методом парабол.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Метод парабол'

    def resolve(self):
        '''Вычисление интеграла методом парабол.'''
        super().resolve()
        a, b = self.range
        n = 0
        s = 0
        s1 = self.error * 10
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x_boof = copy.deepcopy(a)
            s = self.f(a) + self.f(b)

            for i in range(1, split_count):
                x = x_boof + i*h
                if (i % 2 == 0):
                    s += 2*self.f(x)
                else:
                    s += 4*self.f(x)

            s *= h/3
            split_count *= 2
            if self.debug:
                print('{0}: {1}'.format(n, s))

        return resolving.from_dict({'steps': n,
                                    'value': s,
                                    'method_name': self.method_name})