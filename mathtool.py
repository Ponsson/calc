import sys
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
        'Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.')
    sys.exit(0)
if args[0] != "solve":
    print("Ошибка: неизвестная команда. Для справки используйте 'python mathtool.py --help'.")
    sys.exit(1) 

if len(args) == 1:
    a = input("Введите A: ")
    b = input("Введите B: ")
    c = input("Введите C: ")
elif len(args) == 7 and args [1] == "-a" and args[3] == "-b" and args[5] == '-c':
     a = args[2]
     b = args[5]
     c = args[6]

try:
        a = int(input("Введите А: "))
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

if abs(a) > 10000 or abs(b) > 10000 or abs(c) > 10000:
    print('Ошибка: значение вне допустимого диапазона', file=sys.stderr)
    sys.exit(1)
