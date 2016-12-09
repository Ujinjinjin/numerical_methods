class resolving:

    def __init__(self, value, steps, method_name):
        '''Инициализация'''
        self.value = value
        self.steps = steps
        self.method_name = method_name

    def __str__(self):
        '''Вернуть строковое представление обекта'''
        return ('{}: n={};  I={}'.format(self.method_name, self.steps, self.value))

    @classmethod
    def from_dict(cls, dict_solution):
        '''Вернуть объект класса созданный из словаря'''
        if isinstance(dict_solution, dict):
            try:
                value = dict_solution['value']
                steps = dict_solution['steps']
                method_name = dict_solution['method_name']
                return cls(value, steps, method_name)
            except KeyError:
                print('Был передан словарь неверного формата.')
        else:
            raise TypeError('Данный метод создает объект класса "solution" из объекта класса "dict"')
