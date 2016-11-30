import os
import os.path


class func_converter:

    def __init__(self, func_params, func_body):
        '''
        Инициализировать объект. Параметры:
            - func_params(обязательный): параметры передаваемые в создаваемую функцию. Пример: (x, y);
            - func_body(обязательный): тело создаваемой функции; вводится с учетом идентации и синтаксиса Python. Пример: return x * y
        '''

        self.func_params = func_params
        self.func_body = func_body

    def __str__(self):
        '''Вернуть строковое представление объекта класса'''

        return ('После конвертирования будет возвращена следующая функция:'
                '\ndef {}:'
                '\n{}'.format(self.func_params, self.func_body).replace('  ', '..'))

    def convert(self):
        '''
        Вернуть сконвертированную функцию. Возвращается объект класса function.
        Предполагается, что были введены корректные данные.
        '''
        here = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(here, 'templates/func_template.py'), 'r', encoding='utf-8') as f:
            f = f.read()
            f = f.replace('(params)', self.func_params)
            f = f.replace('func_body', self.func_body)

        with open(os.path.join(here, 'templates/new_func.py'), 'w', encoding='utf-8') as new_f:
            new_f.write(f)

        from func.templates.new_func import my_func

        os.remove(os.path.join(here, 'templates/new_func.py'))
        return my_func


if __name__ == '__main__':
    func_params = '(x)'
    func_body = '    return 3*x**2+2*x-6'
    convert = func_converter(func_params, func_body)
    my_func = convert.convert()
    print(my_func(0))


