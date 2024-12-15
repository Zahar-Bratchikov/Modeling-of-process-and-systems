import numpy as np
import matplotlib.pyplot as plt

# Входные параметры
num_counters = 3  # Количество касс
processing_time = 180  # Время обработки покупателя для каждой кассы (в секундах)
arrival_rate = 0.3  # Средняя интенсивность потока покупателей (параметр "a")
total_customers = 500  # Общее количество покупателей
simulations = 1000 # Количество симуляций для усреднения результатов

# Функция для моделирования работы магазина
def simulate_store(num_counters, processing_time, arrival_rate, total_customers):
    service_end_times = np.zeros(num_counters)  # Состояние касс (время окончания обслуживания)
    served_customers = np.zeros(num_counters)  # Количество обслуженных покупателей на каждой кассе
    lost_customers = 0  # Общее количество потерянных покупателей

    current_time = 0  # Текущее время

    for _ in range(total_customers):
        # Определяем интервал до следующего покупателя
        current_time += -np.log(np.random.uniform()) / arrival_rate

        # Проверяем свободные кассы
        free_counters = service_end_times <= current_time
        if free_counters.any():
            # Обслуживаем покупателя на первой свободной кассе
            available_counter = np.argmax(free_counters)  # Находим индекс первой свободной кассы
            service_end_times[available_counter] = current_time + processing_time
            served_customers[available_counter] += 1
        else:
            # Все кассы заняты, покупатель уходит
            lost_customers += 1

    return served_customers, lost_customers

# Многократное моделирование
results = [simulate_store(num_counters, processing_time, arrival_rate, total_customers) for _ in range(simulations)]
served_customers, lost_customers = zip(*results)

# Усреднение результатов
avg_served_customers = np.mean(served_customers, axis=0)
avg_lost_customers = np.mean(lost_customers)

# Вывод результатов
print("Среднее число обслуженных покупателей на кассах:")
for i, val in enumerate(avg_served_customers, 1):
    print(f"Касса {i}: {val:.2f} человек")
print(f"Среднее число потерянных покупателей: {avg_lost_customers:.2f} человек")

# Визуализация результатов
x = np.arange(1, num_counters + 1)

plt.figure(figsize=(8, 5))
plt.bar(x, avg_served_customers, color='lightgreen', label='Обслуженные покупатели')
plt.xlabel('Кассы')
plt.ylabel('Количество покупателей')
plt.title('Среднее количество обслуженных покупателей на каждой кассе')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
