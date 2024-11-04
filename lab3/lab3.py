import math
import random
from tabulate import tabulate

# Параметры линейного конгруэнтного метода
modulus = 10  # модуль M
multiplier = 7  # множитель k
increment = 7  # приращение b
seed = 7  # начальное значение r0
n = 1000000  # количество генерируемых чисел


# Функция генерации псевдослучайных чисел
def lcm(seed):
    return (multiplier * seed + increment) % modulus


# Основная функция
def main():
    data = []  # Массив сгенерированных чисел
    sum_numbers = 0  # Сумма сгенерированных чисел
    current_seed = seed

    for _ in range(n):
        current_seed = lcm(current_seed)
        number = current_seed / modulus  # Нормализация числа в диапазон [0, 1]
        data.append(number)
        sum_numbers += number

    # Математическое ожидание
    math_exp = sum_numbers / n

    # Вычисление дисперсии и стандартного отклонения
    variance = sum((x - math_exp) ** 2 for x in data) / n
    standard_deviation = math.sqrt(variance)

    # Частотный тест
    frequency_test_count = sum(1 for x in data if math_exp - standard_deviation < x < math_exp + standard_deviation)
    frequency_test_result = frequency_test_count / n

    # Проверка на уникальность данных
    uniqueness = "Все элементы уникальные" if len(data) == len(set(data)) else "Есть повторяющиеся элементы"

    # Вычисление вероятностей попадания чисел в интервалы [0, 0.5] и [0.5, 1]
    count_below_half = sum(1 for x in data if x <= 0.5)
    probability_below_half = count_below_half / n * 100
    probability_above_half = 100 - probability_below_half

    # Вывод результатов в виде таблицы
    table = [
        ["Математическое ожидание", math_exp],
        ["Дисперсия", variance],
        ["Среднеквадратичное отклонение", standard_deviation],
        ["Уникальность данных", uniqueness],
        ["Частотный тест", frequency_test_result],
        ["Вероятность попадания до 0.5 (%)", probability_below_half],
        ["Вероятность попадания после 0.5 (%)", probability_above_half]
    ]

    print(tabulate(table, headers=["Показатель", "Значение"], tablefmt="grid"))


# Проверка встроенного генератора
def check_builtin_generator(length):
    generated_numbers = [random.random() for _ in range(length)]
    mean = sum(generated_numbers) / length
    variance = sum((x - mean) ** 2 for x in generated_numbers) / length
    standard_deviation = math.sqrt(variance)

    frequency_test_count = sum(
        1 for x in generated_numbers if mean - standard_deviation < x < mean + standard_deviation)
    frequency_test_result = frequency_test_count / length

    count_below_half = sum(1 for x in generated_numbers if x <= 0.5)
    probability_below_half = count_below_half / length
    probability_above_half = 1 - probability_below_half

    print("\nВстроенный генератор:")
    print(f"Математическое ожидание: {mean}")
    print(f"Дисперсия: {variance}")
    print(f"Среднеквадратичное отклонение: {standard_deviation}")
    print(f"Частотный тест: {frequency_test_result}")
    print(f"Вероятность попадания до 0.5: {probability_below_half}")
    print(f"Вероятность попадания после 0.5: {probability_above_half}")


if __name__ == "__main__":
    main()
    check_builtin_generator(n)
