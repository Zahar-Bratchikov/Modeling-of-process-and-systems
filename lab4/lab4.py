"""
Программа для моделирования работы касс с использованием метода Монте-Карло

Основные переменные:
--------------------
- num_cashiers: Количество касс.
- processing_time: Время обслуживания одного покупателя (в минутах).
- arrival_rate: Интенсивность прихода покупателей (среднее количество покупателей в минуту).
- simulation_time: Время работы системы (в минутах).
- experiments: Количество экспериментов для усреднения результатов.

Классы и методы:
----------------
1. CashierSimulation:
   Класс, моделирующий работу касс.

   Методы:
   - __init__(self, num_cashiers, processing_time, arrival_rate, simulation_time):
     Инициализирует параметры модели, включая количество касс, время обслуживания, интенсивность прихода, время работы и массивы для отслеживания времени окончания обслуживания.

   - generate_next_arrival(self):
     Генерирует время до следующего прихода покупателя с использованием распределения экспоненциального типа.

   - simulate(self):
     Выполняет моделирование процесса обслуживания покупателей с учётом времени работы касс, времени обслуживания и прихода покупателей.

   - results(self):
     Возвращает результаты моделирования в виде словаря с количеством обслуженных и отвергнутых покупателей.

2. main():
   Основная функция:
   - Задает параметры моделирования.
   - Запускает несколько экспериментов и усредняет результаты.
   - Строит график результатов моделирования работы касс, показывающий количество обслуженных покупателей и необслуженных.
"""


import random
import math
import matplotlib.pyplot as plt

class CashierSimulation:
    def __init__(self,  num_cashiers, processing_time, arrival_rate, simulation_time):
        self.num_cashiers = num_cashiers
        self.processing_time = processing_time
        self.arrival_rate = arrival_rate
        self.simulation_time = simulation_time
        self.cashier_end_times = [0] * num_cashiers
        self.served_customers = [0] * num_cashiers
        self.rejected_customers = 0

    def generate_next_arrival(self):
        y = random.uniform(0, 1)
        return -math.log(1 - y) / self.arrival_rate

    def simulate(self):
        current_time = 0
        while current_time < self.simulation_time:
            next_customer_time = self.generate_next_arrival()
            current_time += next_customer_time

            if current_time > self.simulation_time:
                break

            available_cashier = -1
            for i in range(self.num_cashiers):
                if self.cashier_end_times[i] <= current_time:
                    available_cashier = i
                    break

            if available_cashier != -1:
                self.cashier_end_times[available_cashier] = current_time + self.processing_time
                self.served_customers[available_cashier] += 1
            else:
                self.rejected_customers += 1

    def results(self):
        return {
            "served_customers": self.served_customers,
            "rejected_customers": self.rejected_customers,
            "total_served": sum(self.served_customers)
        }


def main():
    # Параметры моделирования
    num_cashiers = 2  # количество касс
    processing_time = 2 # время обслуживания в минутах
    arrival_rate = 0.2 # интенсивность прихода покупателей (кол-во покупателей в минуту)
    simulation_time = 240 # время работы
    experiments = 1000  # Количество экспериментов

    total_served = [0] * num_cashiers
    total_rejected = 0

    for _ in range(experiments):
        simulation = CashierSimulation(num_cashiers, processing_time, arrival_rate, simulation_time)
        simulation.simulate()
        results = simulation.results()
        total_served = [x + y for x, y in zip(total_served, results["served_customers"])]
        total_rejected += results["rejected_customers"]

    # Усредненные результаты
    avg_served = [x / experiments for x in total_served]
    avg_rejected = total_rejected / experiments

    # Округление для целых чисел
    avg_served = [round(x) for x in avg_served]
    avg_rejected = round(avg_rejected)

    print("Результаты моделирования:")
    for i, customers in enumerate(avg_served, 1):
        print(f"Касса {i}: обслужено {customers} покупателей")
    print(f"Среднее количество потерянных покупателей: {avg_rejected}")

    # Построение графика
    labels = [f"Касса {i + 1}" for i in range(num_cashiers)]
    x_positions = list(range(len(labels)))  # Позиции для столбцов

    plt.figure(figsize=(10, 6))

    # Гистограмма для касс
    plt.bar(x_positions, avg_served, color='blue', label="Обслуженные покупатели")

    # Линия для необслуженных покупателей
    plt.plot(
        [min(x_positions) - 0.5, max(x_positions) + 0.5],
        [avg_rejected, avg_rejected],
        color='red', linestyle='--', linewidth=2, label="Необслуженные покупатели"
    )

    # Настройка графика
    plt.xticks(x_positions, labels)
    plt.xlabel("Кассы")
    plt.ylabel("Количество покупателей")
    plt.title("Результаты моделирования работы касс")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()


if __name__ == "__main__":
    main()
