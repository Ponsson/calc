import argparse


def build_parser():
    parser = argparse.ArgumentParser(prog = 'mathtool', description = 'Расчёты над уровнениями и числовыми последовательностями', allow_abbrev = False)
    subparsers = parser.add_subparsers(dest = 'command')

    solve_parser = subparsers.add_parser('solve', help = 'Решение уравнения вида A*x^2 + B*x + C = 0 ', allow_abbrev = False)
    solve_parser.add_argument('-a', type = int, help = 'Коэффициент A')
    solve_parser.add_argument('-b', type = int, help = 'Коэффициент B')
    solve_parser.add_argument('-c', type = int, help = 'Коэффициент C')
    
    stats_parser = subparsers.add_parser('stats', help = 'Расчёты над числовой последовательностью', allow_abbrev = False)
    stats_parser.add_argument('--input', help = 'Входной файл с числовой последовательностью')
    
    series_parser = subparsers.add_parser('series', help = 'Сумма числового ряда', allow_abbrev = False)
    series_parser.add_argument('--func', required = True, choices = ['sqplus', 'rd'], help = 'Введите ряд для суммирования')
    group = series_parser.add_mutually_exclusive_group(required = True)
    group.add_argument('--terms', type = int, help = 'Количество членов ряда')
    group.add_argument('--eps', type = float, help = 'Точность вычислений')

    integrate_parser = subparsers.add_parser('integrate', help='численное интегрирование', allow_abbrev=False)
    integrate_parser.add_argument('--func', required=True, choices=['ratio','root'], help='какую функцию интегрировать')
    integrate_parser.add_argument('--from', dest='lower', type=float, required=True, help='нижний предел')
    integrate_parser.add_argument('--to', dest='upper', type=float, required=True, help='верхний предел')
    integrate_parser.add_argument('--steps', type=int, required=True, help='количество прямоугольников')
    
    return parser