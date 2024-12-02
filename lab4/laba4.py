import numpy as np
import matplotlib.pyplot as plt

# Входные параметры
num_counters = 10  # Количество касс
processing_times = [90] * num_counters # Время обработки покупателя для каждой кассы (в секундах)
arrival_rate = 0.7  # Средняя интенсивность потока покупателей (параметр "a")
total_customers = 1000  # Общее количество покупателей
simulations = 5000  # Количество симуляций для усреднения результатов

# Функция для моделирования работы магазина
def simulate_store(num_counters, processing_times, arrival_rate, total_customers):
    # Инициализация параметров
    service_end_times = np.zeros(num_counters)  # Время, до которого каждая касса занята
    served_customers = np.zeros(num_counters)  # Обслуженные покупатели на каждой кассе
    lost_customers = 0  # Количество потерянных покупателей

    current_time = 0  # Текущее время

    # Симуляция потока покупателей
    for _ in range(total_customers):
        # Время появления следующего покупателя
        arrival_interval = -np.log(np.random.uniform()) / arrival_rate
        current_time += arrival_interval

        # Поиск первой свободной кассы
        free_counters = service_end_times <= current_time
        if np.any(free_counters):
            # Если есть свободная касса, выбираем первую свободную
            available_counter = np.where(free_counters)[0][0]
            service_end_times[available_counter] = current_time + processing_times[available_counter]
            served_customers[available_counter] += 1
        else:
            # Если свободных касс нет, покупатель уходит
            lost_customers += 1

    return served_customers, lost_customers

# Многократное моделирование для усреднения результатов
all_served_customers = []
all_lost_customers = []

for _ in range(simulations):
    served, lost = simulate_store(num_counters, processing_times, arrival_rate, total_customers)
    all_served_customers.append(served)
    all_lost_customers.append(lost)

# Усреднение результатов
avg_served_customers = np.mean(all_served_customers, axis=0)
avg_lost_customers = np.mean(all_lost_customers)

# Вывод результатов
print("Среднее число обслуженных покупателей на кассах:")
for i, val in enumerate(avg_served_customers, 1):
    print(f"Касса {i}: {val:.2f} человек")

print(f"Среднее число потерянных покупателей: {avg_lost_customers:.2f} человек")

# Визуализация результатов
x = np.arange(1, num_counters + 1)
plt.bar(x, avg_served_customers, color='lightgreen', label='Обслуженные покупатели')
plt.xlabel('Кассы')
plt.ylabel('Количество покупателей')
plt.title('Среднее количество обслуженных покупателей на каждой кассе')
plt.legend()
plt.show()
