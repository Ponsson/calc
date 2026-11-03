import math
max_value = 10000
max_range = 20


def check_nums(numbers):
    if len(numbers) == 0:
        raise ValueError("список чисел пуст")
    if len(numbers) > max_range:
        raise ValueError(f"список чисел превышает допустимый диапазон ({max_range})")
    for number in numbers:
        if number is not math.isfinite(number):
            raise ValueError(f"значение {number} не является числом")
        if abs(number) > max_value:
            raise ValueError(f"значение {number} вне допустимого диапазона ({max_value})")