"""
Основные переменные:
--------------------
- g: Ускорение свободного падения (м/с^2).
- L: Дальность стрельбы (м).
- delta: Размер мишени (м).
Функции:
--------
1. calculate_initial_speed(alpha_rad, L):
   Вычисляет начальную скорость для достижения заданной дальности при известном угле.
2. monte_carlo_simulation(n_trials, mv, sigma_v, ma, sigma_a, target_size):
   Выполняет моделирование методом Монте-Карло:
   - Генерирует случайные значения начальной скорости и угла из нормального распределения.
   - Вычисляет дальность выстрела и проверяет попадание в мишень.
   - Возвращает список дальностей и вероятность попадания.
3. calculate_statistics(values):
   Вычисляет математическое ожидание (среднее) и дисперсию для набора значений.
4. plot_combined_results(trial_counts, means, variances, distances, title_suffix):
   Строит графики:
   - Зависимость математического ожидания от числа испытаний.
   - Зависимость дисперсии от числа испытаний.
   - Гистограмму распределения дальностей.
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Константы
g = 9.81  # Ускорение свободного падения, м/с^2
L = 1000  # Дальность стрельбы, м
delta = 30  # Размер мишени, м

# Функция для расчета начальной скорости
def calculate_initial_speed(alpha_rad, L):
    return np.sqrt(L * g / np.sin(2 * alpha_rad))

# Функция для моделирования методом Монте-Карло
def monte_carlo_simulation(n_trials, mv, sigma_v, ma, sigma_a, target_size):
    random = np.random.default_rng()  # Генератор случайных чисел
    distances = []
    hits = 0

    for _ in range(n_trials):
        v = random.normal(mv, sigma_v)  # Скорость из нормального распределения
        alpha_deg = random.normal(ma, sigma_a)  # Угол из нормального распределения
        alpha_rad = np.radians(alpha_deg)
        range_ = (v**2 * np.sin(2 * alpha_rad)) / g

        if L - target_size / 2 <= range_ <= L + target_size / 2:
            hits += 1
        distances.append(range_)

    probability = hits / n_trials
    return distances, probability

# Функция для расчета среднего и дисперсии
def calculate_statistics(values):
    mean = np.mean(values)
    variance = np.var(values, ddof=1)
    return mean, variance

# Построение всех графиков на разных координатных плоскостях
def plot_combined_results(trial_counts, means, variances, distances, title_suffix):
    fig = plt.figure(figsize=(14, 10))
    grid = GridSpec(3, 1, figure=fig)

    # График математического ожидания
    ax1 = fig.add_subplot(grid[0, 0])
    ax1.plot(trial_counts, means, label="Математическое ожидание (M)", color="blue")
    ax1.set_xlabel("Число испытаний")
    ax1.set_ylabel("Математическое ожидание (M)")
    ax1.set_title(f"Математическое ожидание {title_suffix}")
    ax1.grid()
    ax1.legend()

    # График дисперсии
    ax2 = fig.add_subplot(grid[1, 0])
    ax2.plot(trial_counts, variances, label="Дисперсия (D)", color="orange")
    ax2.set_xlabel("Число испытаний")
    ax2.set_ylabel("Дисперсия (D)")
    ax2.set_title(f"Дисперсия {title_suffix}")
    ax2.grid()
    ax2.legend()

    # Гистограмма распределения дальностей
    ax3 = fig.add_subplot(grid[2, 0])
    ax3.hist(distances, bins=50, alpha=0.7, color='blue', edgecolor='black')
    ax3.set_xlabel("Дальность (м)")
    ax3.set_ylabel("Частота")
    ax3.set_title(f"Гистограмма распределения дальностей {title_suffix}")
    ax3.grid()

    plt.tight_layout()
    plt.show()

# Основная программа
def main():
    # Угол стрельбы и начальная скорость
    alpha_deg = 45  # Угол в градусах
    alpha_rad = np.radians(alpha_deg)
    mv = calculate_initial_speed(alpha_rad, L)  # Рассчетная скорость для заданной дальности

    # Параметры нормального распределения
    sigma_v_values = [10, 20]  # Среднеквадратическое отклонение скорости
    sigma_a_values = [np.radians(2), np.radians(5)]  # Среднеквадратическое отклонение угла
    ma = alpha_deg  # Среднее значение угла (в градусах)

    n_trials = 10000  # Количество испытаний
    trial_counts = range(2, n_trials + 1)

    for sigma_v in sigma_v_values:
        for sigma_a in sigma_a_values:
            distances, probability = monte_carlo_simulation(n_trials, mv, sigma_v, ma, sigma_a, delta)

            # Вычисление M и D для каждого количества испытаний
            means, variances = [], []
            for i in trial_counts:
                subset = distances[:i]
                mean, variance = calculate_statistics(subset)
                means.append(mean)
                variances.append(variance)

            print(f"Параметры: σ_v = {sigma_v}, σ_α = {np.degrees(sigma_a):.1f}°")
            print(f"Математическое ожидание (M): {means[-1]:.2f} м")
            print(f"Дисперсия (D): {variances[-1]:.2f} м²")
            print(f"Вероятность попадания: {probability * 100:.2f}%\n")

            # Построение графиков
            plot_combined_results(trial_counts, means, variances, distances, f"(σ_v={sigma_v}, σ_α={np.degrees(sigma_a):.1f}°)")

# Запуск программы
if __name__ == "__main__":
    main()
