from equations.resolving import resolving


class equation_resolving:
    '''Материнский класс для решения уравнений.'''

    def __init__(self, range, base_function=None, derivative=None, sqr_derivative=None, error=0.00001, debug=False):
        '''Инициализация.'''
        # if isinstance(base_function, function) and isinstance(derivative, function) and isinstance(sqr_derivative, function):
        self.base_function = base_function
        self.derivative = derivative
        self.sqr_derivative = sqr_derivative
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

    def f1(self, x):
        '''Первая производная функции вида f'(x)=...'''
        return eval(self.derivative)

    def f2(self, x):
        '''Вторая производная функции вида f''(x)=...'''
        return eval(self.sqr_derivative)

    def resolve(self):
        '''Решить.'''
        self.check_value()
        if self.debug:
            print('{}, error={}'.format(self.method_name, self.error))

    def check_value(self):
        '''Проверка корректности введеного отрезка и погрешности.'''
        if not (isinstance(self.error, float) or isinstance(self.error, int)):
            raise TypeError('Погрешность должна быть объектом класса "int" или "float".')
        if isinstance(self.range, list) and len(self.range) == 2:
            a, b = self.range

            if self.f(a) * self.f(b) > 0:
                raise ValueError('На данном отрезке нет корней, так как на его концах фунция имеет одинаковые знаки.')

            if self.f(a) == 0:
                print('Корнем уравнения на отрезке {} является x={}.'.format(self.range, a))
            if self.f(b) == 0:
                print('Корнем уравнения на отрезке {} является x={}.'.format(self.range, b))
        else:
            raise TypeError('Введен некорректный отрезок {}.'.format(self.range))


class bisection(equation_resolving):
    '''Класс, описывающий логику решения уравнений методом половинного деления.'''

    def __init__(self, range, base_function=None, derivative=None, sqr_derivative=None, error=0.00001, debug=False):
        super().__init__(range, base_function, derivative, sqr_derivative, error=0.00001, debug=debug)
        self.method_name = 'Метод половинного деления'

    def resolve(self):
        '''Поиск корней методом половинного деления.'''
        super().resolve()
        a, b = self.range
        n = 0
        c = a
        while abs(self.f(c)) > self.error:
            n += 1
            c = (a + b) / 2
            if self.debug:
                print('{0}: {1}'.format(n, c))
                # print('{0}: {1}\nf(x)={2}'.format(n, c, self.f(c)))
            if self.f(c) * self.f(a) < 0:
                b = c
            else:
                a = c
        return resolving.from_dict({'steps': n,
                                    'value': c,
                                    'method_name': self.method_name})


class chord(equation_resolving):
    '''Класс, описывающий логику решения уравнений методом хорд.'''

    def __init__(self, range, base_function=None, derivative=None, sqr_derivative=None, error=0.00001, debug=False):
        super().__init__(range, base_function, derivative, sqr_derivative, error=0.00001, debug=debug)
        self.method_name = 'Метод хорд'

    def resolve(self):
        '''Поиск корней методом хорд.'''
        super().resolve()
        a, b = self.range
        n = 0
        c = a
        while abs(self.f(c)) > self.error:
            n += 1
            c = a - (self.f(a)*(b - a)) / (self.f(b) - self.f(a))
            if self.debug:
                print('{0}: {1}'.format(n, c))
                # print('{0}: {1}\nf(x)={2}'.format(n, c, self.f(c)))
            if self.f(c) * self.f(a) < 0:
                b = c
            else:
                a = c

        return resolving.from_dict({'steps': n,
                                    'value': c,
                                    'method_name': self.method_name})


class shearing(equation_resolving):
    '''Класс, описывающий логику решения уравнений методом касательных.'''

    def __init__(self, range, base_function=None, derivative=None, sqr_derivative=None, error=0.00001, debug=False):
        super().__init__(range, base_function, derivative, sqr_derivative, error=0.00001, debug=debug)
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


class combo(equation_resolving):
    '''Класс, описывающий логику решения уравнений комбинированным методом.'''

    def __init__(self, range, base_function=None, derivative=None, sqr_derivative=None, error=0.00001, debug=False):
        super().__init__(range, base_function, derivative, sqr_derivative, error=0.00001, debug=debug)
        self.method_name = 'Комбинированный метод хорд и касательных'

    def resolve(self):
        '''Поиск корней комбинированным методом хорд и касательных.'''
        super().resolve()

        chord_resolve = chord(self.range, self.base_function, self.derivative, self.sqr_derivative).resolve()
        shearing_resolve = shearing(self.range, self.base_function, self.derivative, self.sqr_derivative).resolve()
        x = (chord_resolve.value + chord_resolve.value) / 2
        n = chord_resolve.steps + shearing_resolve.steps

        return resolving.from_dict({'steps': n,
                                    'value': x,
                                    'method_name': self.method_name})
