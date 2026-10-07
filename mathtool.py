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
    a = int(input("Введите А: "))
    b = int(input("Введите B: "))
    c = int(input("Введите C: "))
    