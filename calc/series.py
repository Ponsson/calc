import math
max_terms = 10000
max_eps = 0.0001
max_iter = 100000

def evenodd(n):
    """Возвращает знак n-го члена: для четных -1 и 1 для нечетных"""
    if n % 2 == 0:
        return -1
    return 1 

def term_sqplus(n):
    """Возвращает n-е слагаемое ряда sqplus: ±1/(n^2+1)"""
    return evenodd(n) / (n**2 + 1)

def term_rd(n):
    """Возвращает n-е слагаемое ряда third: ±1/(3n)"""
    return evenodd(n) / (n*3)

FRMLS = {
    "sqplus": (term_sqplus, 'S = 1/(1^2 + 1) - 1/(2^2 + 1) + 1/(3^2 + 1) - ...'),
    "rd": (term_rd, 'S = 1/3 - 1/6 + 1/9 - ...')
}

def sum_by_term(term, count):
    """Суммирует count первых слагаемых ряда term"""
    res = 0
    for n in range(1, count + 1):
        res += term(n)
    return res

def sum_by_eps(term, eps):
    """Суммирует слагаемые ряда term, пока очередное не станет меньше eps по модулю"""
    res = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        res += value
        if abs(value) < eps:
            return res, n
        if n >= max_iter:
            raise ValueError(f"не удалось достичь точности {eps} за {max_iter} итераций")

def check_terms(terms):
    """Проверяет на количество слагаемых"""    
    if terms < 1 or terms > max_terms:
        raise ValueError(f"количество членов ряда должно быть в диапазоне от 1 до {max_terms}")

def check_eps(eps):
    """Проверяет на точность"""
    if not math.isfinite(eps) or eps <= 0 or eps > max_eps:
        raise ValueError(f"точность вне диапазона [0, {max_eps}]")    