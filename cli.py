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
    return parser 