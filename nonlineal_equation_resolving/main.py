from func.converter import func_converter
from equations.resolving_methods import *
import time


if __name__ == '__main__':

    def f(x):
        return eval('x**3 - 3*x + 7')

    def ff(x):
        return x**3 - 3*x + 7

    def f1(x):
        return 3*x**2 - 3

    def f2(x):
        return 6*x

    # for i in range(-5, 5):
    #     print(f(i), ff(i))

    range = [-3, -2]
    shear = shearing()
    shear.enter_function()
    print(shear.resolve(range))