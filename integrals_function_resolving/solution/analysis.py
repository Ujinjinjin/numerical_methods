from equations.resolving_methods import *
import pylab
import copy
pylab.rcParams['font.sans-serif'] = ['Arial']


class analyzer:
    '''Класс, позволяющий проводить анализ эффективности методов решения'''

    def __init__(self, *methods, min_error=0.00001, max_error=0.0001, error_step=0.00001):
        '''
        Инициализировать объект класса. Предполагается, что в качестве параметров
        будут переданы корректные данные (т.е. объекты класса resolving_method с
        корректно заполнеными полями)'''
        
        if isinstance(methods[0], list):
            methods = methods[0]

        self.methods = methods
        self.min_error = min_error
        self.max_error = max_error
        self.error_step = error_step
        self.method_names = []
        self.method_steps = []

    def annalyze(self):
        '''Получить результаты эфективности решения задачи каждым методом.'''

        for method in self.methods:

            self.method_names.append(method.method_name)

            current_error = self.min_error
            steps = []

            while current_error <= self.max_error:
                method.error = current_error
                solution = method.resolve()
                steps.append(copy.deepcopy(solution.steps))
                current_error += self.error_step
            
            self.method_steps.append(steps)

    def graph(self):
        '''Построить график эфективности каждого метода.'''

        sx = [i * self.error_step for i in range(1, int((self.max_error - self.min_error) / self.error_step) + 2)]
        pylab.plot(sx, [0 for i in sx], linewidth=0)
        for i, method in enumerate(self.method_names):
            pylab.plot(sx, self.method_steps[i], label=method, linewidth=3)

        pylab.title('График эффективности')
        pylab.xlabel('E')
        pylab.ylabel('Steps')
        pylab.legend(loc = 'upper right')

        pylab.show()
        

    def run(self):
        '''Запустить программу.'''

        self.annalyze()
        self.graph()