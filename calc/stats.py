import math
max_value = 10000
max_range = 20


def check_nums(numbers):
    if len(numbers) == 0:
        raise ValueError("список чисел пуст")
    if len(numbers) > max_range:
        raise ValueError(f"список чисел превышает допустимый диапазон ({max_range})")
    for number in numbers:
        if not math.isfinite(number):
            raise ValueError(f"значение {number} - недопустимое число")
        if abs(number) > max_value:
            raise ValueError(f"значение {number} вне допустимого диапазона ({max_value})")


def sum(numbers):
    res = 0 
    for number in numbers:
        res += number
    return res
def mean(numbers):
    return sum(numbers) / len(numbers)
def sum_squares(numbers):
    res = 0
    for number in numbers:
        res += number**2
    return res
def sqr_mean(numbers):
    return math.sqrt(sum_squares(numbers) / len(numbers))
def sum_sqr_dev(numbers):
    avg = mean(numbers)
    res = 0
    for number in numbers:
        res += (number - avg)**2
    return res
def var(numbers):
    return sum_sqr_dev(numbers) / len(numbers)
def sqr_dev(numbers):
    return math.sqrt(var(numbers)
def st_dev(numbers):
    if len(numbers) < 2:
        return 0
    return math.sqrt(sum_sqr_dev(numbers) / (len(numbers) - 1))
def min(numbers):
    res = numbers[0]
    for number in numbers:
        if number < res:
            res = number
    return res
def max(numbers):
    res = numbers[0]
    for number in numbers:
        if number > res:
            res = number
    return res
def cntplus(numbers):
    res = 0
    for number in numbers:
        if number > 0:
            res += 1
    return res
def cntmns(numbers):
    res = 0
    for number in numbers:
        if number < 0:
            res += 1
    return res


end = [
    ('Сумма', sum, '.3f'),
    ('Среднее', mean, '.3f'),
    ('Сумма квадратов', sum_squares, '.3f'),
    ('Среднее квадратичное', sqr_mean, '.3f'),
    ('Сумма квадратов отклонений', sum_sqr_dev, '.3f'),
    ('Дисперсия', var, '.3f'),
    ('Среднеквадратичное отклонение', sqr_dev, '.3f'),
    ('Исправленное среднеквадратичное отклонение', st_dev, '.3f'),
    ('Минимум', min, '.3f'),
    ('Максимум', max, '.3f'),
    ('Количество положительных чисел', cntplus, 'd'),
    ('Количество отрицательных чисел', cntmns, 'd')
]