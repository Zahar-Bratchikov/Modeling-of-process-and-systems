import random

def shop_simulation():
    num_cashiers = int(input("Введите кол-во кассиров: "))
    processing_time = int(input("Введите время обслуживания 1 клиента (в секундах): "))
    num_simulations = int(input("Введите кол-во симуляций: "))
    current_time = int(input("Введите начальное время (в секундах): "))
    total_work_time = int(input("Введите время работы (в часах): ")) * 60 * 60

    # Инициализация переменных
    total_customers_served = [0] * num_cashiers
    total_customers_lost = 0
    status_customers = [False] * num_cashiers
    service_time_customers = [0] * num_cashiers

    for simulation in range(num_simulations):
        current_time = 0

        while current_time < total_work_time:
            arrival_rate = random.randint(1, 50)

            if arrival_rate > total_work_time - current_time:
                break

            current_time += arrival_rate

            for i in range(num_cashiers):
                if service_time_customers[i] != 0:
                    if service_time_customers[i] <= arrival_rate:
                        service_time_customers[i] = 0
                        status_customers[i] = False
                        total_customers_served[i] += 1
                    else:
                        service_time_customers[i] -= arrival_rate

            at_least_one_cashier_free = any(not status for status in status_customers)

            if not at_least_one_cashier_free:
                total_customers_lost += 1
            else:
                for i in range(num_cashiers):
                    if not status_customers[i]:
                        status_customers[i] = True
                        service_time_customers[i] = processing_time
                        break

    average_customers_served = [total // num_simulations for total in total_customers_served]

    print("Количество обслуженных клиентов каждой кассой:", " ".join(map(str, average_customers_served)))
    print("Количество необслуженных клиентов:", total_customers_lost // num_simulations)


if __name__ == "__main__":
    shop_simulation()
