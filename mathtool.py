import math
import sys
from calc import equation
from cli import build_parser
parser = build_parser()
args = parser.parse_args()

if args.command is None:
    parser.print_help()
    sys.exit(0)



if args.a is None and args.b is None and args.c is None:
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    except ValueError:
        print("Ошибка: заданный коэффициент не является числом", file=sys.stderr)
        sys.exit(1)
elif args.a is not None and args.b is not None and args.c is not None:  
    a = args.a
    b = args.b
    c = args.c
else:
    print('Ошибка: введите все 3 коэффициента либо ни одного', file=sys.stderr)
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
        if d == 0:
            print(f'Уравнение {kind}\n D = {d}\n Действительный корень: {roots[0]:.3f}')
        else:
            print(f'Уравнение {kind}\n D = {d}\n Действительные корни: {roots[0]:.3f}, {roots[1]:.3f}')
    else:
        print(f'Уравнение {kind}\n Действительный корень: {roots:.3f}')
