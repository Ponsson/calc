import math
import sys
from calc import equation
from cli import build_parser
parser = build_parser()
args = parser.parse_args()

if args.command is None:
    parser.print_help()
    sys.exit(0)




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


try:
    equation.check_coef(a, b, c)
except ValueError as error:
    print(error, file=sys.stderr)
    sys.exit(1)

kind, d, roots = equation.solve(a, b, c)
if roots is None:
    print(f'Уравнение {kind}\n D = {d}\n Действительных корней нет')
else:
    if kind == 'квадратное':
        print(f'Уравнение {kind}\n D = {d}\n Действительные корни: {roots:.3f}')
    else:
        print(f'Уравнение {kind}\n x = {roots:.3f}')
