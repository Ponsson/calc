import sys
from calc import equation
from cli import build_parser

def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
        try:
            a_s = int(input("Введите A: "))
            b_s = int(input("Введите B: "))
            c_s = int(input("Введите C: "))
        except ValueError:
            raise ValueError("заданный коэффициент не является числом")
    elif args.a is not None and args.b is not None and args.c is not None:
        a_s = args.a
        b_s = args.b
        c_s = args.c
    else:
        raise ValueError("введите все 3 коэффициента либо ни одного")
    try:
        a = int(a_s)
        b = int(b_s)    
        c = int(c_s)
    except ValueError:
        raise ValueError("заданный коэффициент не является числом")
    equation.check_coef(a, b, c)


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

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        if args.command == 'solve':
            return handle_solve(args)
    except ValueError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))