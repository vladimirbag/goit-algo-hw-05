import re
from typing import Callable

def generator_numbers(text):
    pattern = r'(?<!\S)[+-]?\d*\.?\d+(?!\S)' # Регулярний вираз для дійсних чисел
    for match in re.findall(pattern, text):
        yield float(match)  # Повертаємо числа як float

def sum_profit(text, func: Callable):
    return sum(func(text))  # Викликаємо переданий генератор і підсумовуємо числа


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід," 
"доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")