# from equations.resolving import resolving
from resolving import resolving
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
        s1 = self.error + 1
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x = copy.deepcopy(a)
            for i in range(0, split_count):
                x += h
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
        s1 = self.error + 1
        split_count = 10  # Кол-во разбиений
        while abs(s - s1) >= self.error:
            n += 1

            s1 = copy.deepcopy(s)
            s = 0
            h = (b - a) / split_count
            x = copy.deepcopy(a)
            for i in range(1, split_count+1):
                x += h
                s += self.f(x)

            s *= h
            split_count *= 2
            if self.debug:
                print('{0}: {1}'.format(n, s))
        return resolving.from_dict({'steps': n,
                                    'value': s,
                                    'method_name': self.method_name})


class middle_rect(integrals_resolving):
    '''Класс, описывающий логику решения уравнений методом касательных.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Метод касательных'

    def resolve(self):
        '''Поиск корней методом касательных.'''
        super().resolve()
        a, b = self.range
        n = 0

        if self.f(a)*self.f2(a)>0:
            c = a
        else:
            c = b
        while abs(self.f(c)) > self.error:
            n += 1
            c = c - (self.f(c) / self.f1(c))
            if self.debug:
                print('{0}: {1}'.format(n, c))
                # print('{0}: {1}\nf(x)={2}'.format(n, c, self.f(c)))

        return resolving.from_dict({'steps': n,
                                   'value': c,
                                   'method_name': self.method_name})


class trapeze(integrals_resolving):
    '''Класс, описывающий логику решения уравнений комбинированным методом.'''

    def __init__(self, range, base_function=None, error=0.001, debug=False):
        super().__init__(range, base_function, error=error, debug=debug)
        self.method_name = 'Комбинированный метод хорд и касательных'

    def resolve(self):
        '''Поиск корней комбинированным методом хорд и касательных.'''
        super().resolve()

        x = (chord_resolve.value + chord_resolve.value) / 2
        n = chord_resolve.steps + shearing_resolve.steps

        return resolving.from_dict({'steps': n,
                                    'value': x,
                                    'method_name': self.method_name})


class parabola(integrals_resolving):
    ''''''
    pass



if __name__=="__main__":

    left = left_rect([2, 5], 'x**2', 0.1)
    right = right_rect([2, 5], 'x**2', 0.1)
    print(left.resolve())
    print(right.resolve())