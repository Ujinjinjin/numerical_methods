from equations.resolving import resolving


class equation_resolving:

    def __init__(self, base_function=None, derivative=None, sqr_derivative=None, error=0.00001):
        '''Инициализация'''
        # if isinstance(base_function, function) and isinstance(derivative, function) and isinstance(sqr_derivative, function):
        self.base_function = base_function
        self.derivative = derivative
        self.sqr_derivative = sqr_derivative
        self.error = error
        self.method_name = None
        # else:
        #    raise TypeError('ОШИБКА. В конструктор был передан объект не являющийся объектом класса "function"')
    
    def f(self, x):
        '''Основная функция вида f(x)=...'''
        return eval(self.base_function)

    def f1(self, x):
        '''Первая производная функции вида f'(x)=...'''
        return eval(self.derivative)

    def f2(self, x):
        '''Вторая производная функции вида f''(x)=...'''
        return eval(self.sqr_derivative)

    def enter_function(self):
        '''Ввести функцию, для которой нужно найти корни, и ее производные.'''
        self.base_function = input("f(x)=")
        self.derivative = input("f'(x)=")
        self.sqr_derivative = input("f''(x)=")


    def resolve(self, range):
        '''Решить'''
        self.check_value(range)
        print(self.method_name)
        pass

    def check_value(self, range):
        '''Проверка корректности введеного отрезка и погрешности'''
        if not (isinstance(self.error, float) or isinstance(self.error, int)):
            raise TypeError('Погрешность должна быть объектом класса "int" или "float"')
        if isinstance(range, list) and len(range) == 2:
            a, b = range

            if self.f(a) * self.f(b) > 0:
                raise ValueError('На данном отрезке нет корней, так как на его концах фунция имеет одинаковые знаки.')

            if self.f(a) == 0:
                print('Корнем уравнения на отрезке {} является x={}'.format(range, a))
            if self.f(b) == 0:
                print('Корнем уравнения на отрезке {} является x={}'.format(range, b))
        else:
            raise TypeError('Введен некорректный отрезок {}.'.format(range))


class bisection(equation_resolving):

    def __init__(self, base_function=None, derivative=None, sqr_derivative=None, error=0.00001):
        super().__init__(base_function, derivative, sqr_derivative, error=0.00001)
        self.method_name = 'Метод половинного деления'

    def resolve(self, range):
        '''Поиск корней методом половинного деления'''
        super().resolve(range)
        a, b = range
        n = 0
        c = a
        while abs(self.f(c)) > self.error:
            n += 1
            c = (a + b) / 2
            #print('{0}: {1}'.format(n, c))
            print('{0}: {1}\nf(x)={2}'.format(n, c, self.f(c))) 
            if self.f(c) * self.f(a) < 0:
                b = c
            else:
                a = c
        return resolving.from_dict({'steps': n,
                                    'value': c,
                                    'method_name': 'Метод половинного деления'})


class chord(equation_resolving):

    def __init__(self, base_function=None, derivative=None, sqr_derivative=None, error=0.00001):
        super().__init__(base_function, derivative, sqr_derivative, error=0.00001)
        self.method_name = 'Метод хорд'

    def resolve(self, range):
        '''Поиск корней методом хорд'''
        super().resolve(range)
        a, b = range
        n = 0
        c = a
        while abs(self.f(c)) > self.error:
            n += 1
            c = a - (self.f(a)*(b - a)) / (self.f(b) - self.f(a))
            #print('{0}: {1}'.format(n, c))
            print('{0}: {1}\nf(x)={2}'.format(n, c, self.f(c))) 
            if self.f(c) * self.f(a) < 0:
                b = c
            else:
                a = c

        return resolving.from_dict({'steps': n,
                                    'value': c,
                                    'method_name': 'Метод хорд'})


class shearing(equation_resolving):

    def __init__(self, base_function=None, derivative=None, sqr_derivative=None, error=0.00001):
        super().__init__(base_function, derivative, sqr_derivative, error=0.00001)
        self.method_name = 'Метод касательных'

    def resolve(self, range):
        '''Поиск корней методом касательных'''
        super().resolve(range)
        a, b = range
        n = 0

        if self.f(a)*self.f2(a)>0:
            c = a
        else:
            c = b
        while abs(self.f(c)) > self.error:
            n += 1
            c = c - (self.f(c) / self.f1(c))
            #print('{0}: {1}'.format(n, c))
            print('{0}: {1}\nf(x)={2}'.format(n, c, self.f(c))) 

        return resolving.from_dict({'steps': n,
                                   'value': c,
                                   'method_name': 'Метод касательных'})


class combo(equation_resolving):

    def __init__(self, base_function=None, derivative=None, sqr_derivative=None, error=0.00001):
        super().__init__(base_function, derivative, sqr_derivative, error=0.00001)
        self.method_name = 'Комбинированный метод хорд и касательных'

    def resolve(self, range):
        '''Поиск корней комбинированным методом хорд и касательных'''
        super().resolve(range)

        chord_resolve = chord(self.f, self.f1, self.f2).resolve(range)
        shearing_resolve = shearing(self.f, self.f1, self.f2).resolve(range)
        x = (chord_resolve.value + chord_resolve.value) / 2
        n = chord_resolve.steps + shearing_resolve.steps

        return resolving.from_dict({'steps': n,
                                    'value': x,
                                    'method_name': 'Комбинированный метод хорд и касательных'})



if __name__ == '__main__':

    def f(x):
        return x**3-3*x+7
    def f1(x):
        return 3*x**2-3
    def f2(x):
        return 6*x

    range = [-3, -2]
    error = 0.00001
    print(bisection(f, f1, f2).resolve(range))