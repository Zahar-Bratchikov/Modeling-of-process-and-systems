import random
import time
import math


class LCG:
    def __init__(self, seed, k, b, m):
        self.r = seed
        self.k = k
        self.b = b
        self.m = m

    def generate(self, n):
        random_numbers = []
        for _ in range(n):
            self.r = (self.k * self.r + self.b) % self.m
            random_numbers.append(self.r / self.m)
        return random_numbers


def get_mean(random_numbers):
    return sum(random_numbers) / len(random_numbers)


def get_variance(random_numbers, mean):
    return sum((x - mean) ** 2 for x in random_numbers) / len(random_numbers)


def get_count_interval(random_numbers, x1, x2):
    return sum(1 for x in random_numbers if x1 <= x <= x2)


def gsph(random_numbers):
    seen = set()
    for i, num in enumerate(random_numbers, start=1):
        if num in seen:
            print(f"Обнаружено повторение: {num}")
            return i
        seen.add(num)
    return len(random_numbers)


def compare_with_builtin_generator(n):
    random_numbers = [random.random() for _ in range(n)]

    print("Встроенный генератор")
    mean = get_mean(random_numbers)
    print(f"Математическое ожидание: {mean}")

    variance = get_variance(random_numbers, mean)
    print(f"Дисперсия: {variance}")

    std_deviation = math.sqrt(variance)
    print(f"Стандартное отклонение: {std_deviation}")

    count_in_interval = get_count_interval(random_numbers, 0, 0.5)
    print(f"Процент чисел в интервале [0, 0.5]: {count_in_interval / n * 100:.2f}%")

    count_in_interval = get_count_interval(random_numbers, mean - std_deviation, mean + std_deviation)
    print(f"Прохождение частотного теста: {count_in_interval / n * 100:.2f}%")

    print(f"Длина периода (количество значений до первого повторения): {gsph(random_numbers)}")


def main():
    seed = int(time.time())
    n = 1000000
    k = 162147
    b = 107803
    m = 2**21


    lcg = LCG(seed, k, b, m)
    random_numbers = lcg.generate(n)

    print("Реализованная генерация")
    mean = get_mean(random_numbers)
    print(f"Математическое ожидание: {mean}")

    variance = get_variance(random_numbers, mean)
    print(f"Дисперсия: {variance}")

    std_deviation = math.sqrt(variance)
    print(f"Стандартное отклонение: {std_deviation}")

    count_in_interval = get_count_interval(random_numbers, 0, 0.5)
    print(f"Процент чисел в интервале [0, 0.5]: {count_in_interval / n * 100:.2f}%")

    count_in_interval = get_count_interval(random_numbers, mean - std_deviation, mean + std_deviation)
    print(f"Прохождение частотного теста: {count_in_interval / n * 100:.2f}%")

    print(f"Длина периода (количество значений до первого повторения): {gsph(random_numbers)}")

    print("\n---------------------------------------------------------------\n")

    compare_with_builtin_generator(n)
    """проверка генерации и вывода одного или нескольких чисел"""
    # print("\n---------------------------------------------------------------\n")
    # random_numbers = lcg.generate(3)
    # print(random_numbers[1])

if __name__ == "__main__":
    main()
