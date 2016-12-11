from solution.solution import *


if __name__ == '__main__':
    while True:
        try:
            choise = input('\nЖелаете провести анализ эффективности методов?(y/n): ').lower()
            if choise == 'y' or choise == 'yes':
                analyze = True
            elif choise == 'n' or choise == 'no':
                analyze = False
            else:
                raise ValueError
            break
        except ValueError:
            print('Команда не распознана. Попробуйте еще раз.')
    
    sol = solution(analyze=analyze)
    sol.run()

    input()

    # range = [-3, -2]
    # f = 'x**3 - 3*x + 7'
    # f1 = '3*x**2 - 3'
    # f2 = '6*x'