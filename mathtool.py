import sys
from calc import equation
from calc import stats
from calc import series
from calc import integrate
from cli import build_parser

def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
        try:
            a_s = int(input("Введите A: "))
        except ValueError:
            raise ValueError("заданный коэффициент не является числом")
        equation.check_range('A', a_s)
        try:
            b_s = int(input("Введите B: "))
        except ValueError:
            raise ValueError("заданный коэффициент не является числом")
        equation.check_range('B', b_s)
        try:
            c_s = int(input("Введите C: "))
        except ValueError:
            raise ValueError("заданный коэффициент не является числом")
        equation.check_range('C', c_s)
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
            print(f'Уравнение {kind}\n Действительный корень: {roots[0]:.3f}')

def handle_stats(args):
    if args.input:
        with open(args.input, encoding = 'utf-8-sig') as handle:
            numbers = read_numbers(handle)
    else:
        numbers = read_numbers(sys.stdin)
    stats.check_nums(numbers)
    print(f'Количество: {len(numbers)}')
    for lab, func, form in stats.end:
        value = func(numbers)
        if value is None:
            print(f'{lab}: не существует')
        else:
            print(f'{lab}: {value:{form}}')
    return 0


def read_numbers(src):
    numbers = []
    for line in src:
        for wd in line.split():
            try:
                number = float(wd)
            except ValueError:
                raise ValueError(f"значение {wd} не является числом")
            numbers.append(number)
    return numbers

def handle_series(args):
    term, form = series.FRMLS[args.func]

    if args.terms is not None:
        series.check_terms(args.terms)
        res = series.sum_by_term(term, args.terms)
        count = args.terms
    else:
        series.check_eps(args.eps)
        res, count = series.sum_by_eps(term, args.eps)

    print(form)
    print(f'Количество членов ряда: {count}')
    print(f'Сумма ряда: {res:.4f}')
    return 0

def handle_integrate(args):
    func, form, low, high, inclusive = integrate.FUNCS[args.func]

    integrate.check_bounds(args.lower, args.upper, low, high, inclusive)
    integrate.check_steps(args.steps)

    print(form)
    res = integrate.integrate(func, args.lower, args.upper, args.steps)
    print(f'Значение интегралла: {res:.4f}')
    return 0





def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        if args.command == 'solve':
            return handle_solve(args)
        elif args.command == 'stats':
            return handle_stats(args)
        elif args.command == 'series':
            return handle_series(args)
        elif args.command == 'integrate':
            return handle_integrate(args)
    except (ValueError, OSError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))