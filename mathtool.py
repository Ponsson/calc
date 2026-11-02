import math
import sys
import equation from calc
args = sys.argv[1:]
if len(args) == 0 or args[0] == "--help":
    print('mathtool — консольное приложение для решения алгебраических уравнений вида A*x^2 + B*x + C = 0,\n'
        'где A, B, C — коэффициенты уравнения, задаваемые пользователем.\n'
        'Приложение вычисляет и выводит действительные корни уравнения.\n'
        '\n'
        'Доступные команды:\n'
        '  python mathtool.py                          — вывод справки\n'
        '  python mathtool.py --help                   — вывод справки\n'
        '  python mathtool.py solve                    — ввод коэффициентов с клавиатуры\n'
        '  python mathtool.py solve -a 1 -b 1 -c 1     — решение с заданными коэффициентами\n'
        '\n'
        f'Коэффициенты A, B, C — целые числа, по модулю не превышающие {max_value}.')
    sys.exit(0)
if args[0] != "solve":
    print("Ошибка: неизвестная команда. Для справки используйте 'python mathtool.py --help'.")
    sys.exit(1) 




if len(args) == 1:
    try:
        a = int(input("Введите A: "))
    except ValueError:
        print("Ошибка: заданный коэффициент не является числом", file=sys.stderr)
        sys.exit(1)
    try:
        b = int(input("Введите B: "))
    except ValueError:
        print("Ошибка: заданный коэффициент не является числом", file=sys.stderr)
        sys.exit(1)
    try:
        c = int(input("Введите C: "))
    except ValueError:
        print("Ошибка: заданный коэффициент не является числом", file=sys.stderr)
        sys.exit(1)
elif len(args) == 7 and args [1] == "-a" and args[3] == "-b" and args[5] == '-c':
    a = args[2]
    b = args[4]
    c = args[6]
else:
    print('Ошибка: неверный формат ввода', file=sys.stderr)
    sys.exit(1)
try:
    a = int(a)
    b = int(b)    
    c = int(c)
except ValueError:
    print("Ошибка: заданный коэффициент не является числом", file=sys.stderr)
    sys.exit(1)

kind, d, roots = equation.solve(a, b, c)
if roots is None:
    print(f'Уравнение {kind}\n D = {d}\n Действительных корней нет')
else:
    print(f'Уравнение {kind}\n D = {d}\n x = {roots}')
