import math
max_steps = 10000

def func_ratio(x):
    """Вычисляет значение функции x/(x+1) в точке x"""
    return x / (x+1)

def func_root(x):
    """Вычисляет значение функции sqrt(x^2+1) в точке x."""
    return math.sqrt(x**2 + 1)

def check_steps(steps):
    """Проверяет, что количество прямоугольников steps в диапазоне 1-max_steps."""
    if steps < 1 or steps > max_steps:
        raise ValueError(f"количество прямоугольников должно быть в диапазоне от 1 до {max_steps}")

FUNCS = {
    'ratio': (func_ratio, 'F(x) = x/(x+1)', 0, 20, True),
    'root': (func_root, 'F(x) = sqrt(x^2 + 1)', -5, 5, False)
}

def integrate(func, a, b, steps):
    """Вычисляет интеграл функции func на промежутке [a,b] методом левых прямоугольников"""   
    dx = (b - a) / steps
    res = 0
    for i in range(steps):
        x = a + i * dx
        res += func(x) * dx
    return res

def check_bounds(a,b,low,high,inclusive):
    """Проверяет пределы интегрирования: конечность, порядок и попадание в промежуток функции."""
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError('предел должен быть конечным числом')
    if a >= b:
        raise ValueError('левая граница должна быть меньше правой')
    if inclusive:
        if a < low or a > high or b < low or b > high:
            raise ValueError(f'предел вне промежутка [{low},{high}]')
    else:
        if a <= low or a >= high or b <= low or b >= high:
            raise ValueError(f'предел вне промежутка [{low},{high}]')
