import random

# Состояния
states = [
    "Нагрев-включена подсветка",
    "Нагрев-выключена подсветка",
    "Поддержание температуры-включена подсветка",
    "Поддержание температуры-выключена подсветка",
    "Выключен-включена подсветка",
    "Выключен-выключена подсветка"
]
current_state = states[5]  # Начальное состояние "Выключен-выключена подсветка"

# Переходы с вероятностями (на основе таблицы)
transition_probabilities = {
    "Выключен-включена подсветка": {
        "Включить": [("Нагрев-включена подсветка", 0.4), ("Нагрев-выключена подсветка", 0.1),
                     ("Поддержание температуры-включена подсветка", 0.3), ("Поддержание температуры-выключена подсветка", 0.1),
                     ("Выключен-включена подсветка", 0.05), ("Выключен-выключена подсветка", 0.05)],

        "Температура достигнута": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                                   ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                                   ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)],
        "Охлаждение": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)],
        "Выключить": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)]
    },
    "Выключен-выключена подсветка": {
        "Включить": [("Нагрев-включена подсветка", 0.4), ("Нагрев-выключена подсветка", 0.1),
                     ("Поддержание температуры-включена подсветка", 0.3), ("Поддержание температуры-выключена подсветка", 0.1),
                     ("Выключен-включена подсветка", 0.05), ("Выключен-выключена подсветка", 0.05)],

        "Температура достигнута": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                                   ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                                   ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)],
        "Охлаждение": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)],
        "Выключить": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)]
    },
    "Нагрев-включена подсветка": {
        "Включить": [("Нагрев-включена подсветка", 0.8), ("Нагрев-выключена подсветка", 0.1),
                     ("Поддержание температуры-включена подсветка", 0.025), ("Поддержание температуры-выключена подсветка", 0.025),
                     ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],

        "Температура достигнута": [("Нагрев-включена подсветка", 0.025), ("Нагрев-выключена подсветка", 0.025),
                                   ("Поддержание температуры-включена подсветка", 0.8), ("Поддержание температуры-выключена подсветка", 0.1),
                                   ("Выключен-включена подсветка", 0.05), ("Выключен-выключена подсветка", 0.05)],
        "Охлаждение": [("Нагрев-включена подсветка", 0.8), ("Нагрев-выключена подсветка", 0.1),
                       ("Поддержание температуры-включена подсветка", 0.025), ("Поддержание температуры-выключена подсветка", 0.025),
                       ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],
        "Выключить": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)]
    },
    "Нагрев-выключена подсветка": {
        "Включить": [("Нагрев-включена подсветка", 0.8), ("Нагрев-выключена подсветка", 0.1),
                     ("Поддержание температуры-включена подсветка", 0.025), ("Поддержание температуры-выключена подсветка", 0.025),
                     ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],

        "Температура достигнута": [("Нагрев-включена подсветка", 0.025), ("Нагрев-выключена подсветка", 0.025),
                                   ("Поддержание температуры-включена подсветка", 0.8), ("Поддержание температуры-выключена подсветка", 0.1),
                                   ("Выключен-включена подсветка", 0.05), ("Выключен-выключена подсветка", 0.05)],
        "Охлаждение": [("Нагрев-включена подсветка", 0.8), ("Нагрев-выключена подсветка", 0.1),
                       ("Поддержание температуры-включена подсветка", 0.025), ("Поддержание температуры-выключена подсветка", 0.025),
                       ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],
        "Выключить": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)]
    },
    "Поддержание температуры-включена подсветка": {
        "Включить": [("Нагрев-включена подсветка", 0.025), ("Нагрев-выключена подсветка", 0.025),
                     ("Поддержание температуры-включена подсветка", 0.8), ("Поддержание температуры-выключена подсветка", 0.1),
                     ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],

        "Температура достигнута": [("Нагрев-включена подсветка", 0.025), ("Нагрев-выключена подсветка", 0.025),
                                   ("Поддержание температуры-включена подсветка", 0.8), ("Поддержание температуры-выключена подсветка", 0.1),
                                   ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],
        "Охлаждение": [("Нагрев-включена подсветка", 0.8), ("Нагрев-выключена подсветка", 0.1),
                       ("Поддержание температуры-включена подсветка", 0.025), ("Поддержание температуры-выключена подсветка", 0.025),
                       ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],
        "Выключить": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)]
    },
    "Поддержание температуры-выключена подсветка": {
        "Включить": [("Нагрев-включена подсветка", 0.025), ("Нагрев-выключена подсветка", 0.025),
                     ("Поддержание температуры-включена подсветка", 0.8), ("Поддержание температуры-выключена подсветка", 0.1),
                     ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],

        "Температура достигнута": [("Нагрев-включена подсветка", 0.025), ("Нагрев-выключена подсветка", 0.025),
                                   ("Поддержание температуры-включена подсветка", 0.8), ("Поддержание температуры-выключена подсветка", 0.1),
                                   ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],
        "Охлаждение": [("Нагрев-включена подсветка", 0.8), ("Нагрев-выключена подсветка", 0.1),
                       ("Поддержание температуры-включена подсветка", 0.025), ("Поддержание температуры-выключена подсветка", 0.025),
                       ("Выключен-включена подсветка", 0.025), ("Выключен-выключена подсветка", 0.025)],
        "Выключить": [("Нагрев-включена подсветка", 0.02), ("Нагрев-выключена подсветка", 0.02),
                       ("Поддержание температуры-включена подсветка", 0.02), ("Поддержание температуры-выключена подсветка", 0.02),
                       ("Выключен-включена подсветка", 0.02), ("Выключен-выключена подсветка", 0.9)]
    }
}

# Выходы (индикаторы состояния)
outputs = {
    "Выключен-включена подсветка": "Горит подсветка",
    "Выключен-выключена подсветка": "Подсветка не горит",
    "Нагрев-включена подсветка": "Греется с включенной подсветкой",
    "Нагрев-выключена подсветка": "Греется с выключенной подсветкой",
    "Поддержание температуры-включена подсветка": "Поддержание температуры с включенной подсветкой",
    "Поддержание температуры-выключена подсветка": "Поддержание температуры с выключенной подсветкой"
}

# Функция для выполнения перехода в зависимости от текущего сигнала
def handle_signal(signal):
    global current_state
    if signal in transition_probabilities[current_state]:
        transitions = transition_probabilities[current_state][signal]

        if transitions:
            states, probabilities = zip(*transitions)
            new_state = random.choices(states, probabilities)[0]
            probability = dict(transitions)[new_state]
            current_state = new_state
            print(f"Переход в состояние: {current_state} ({outputs[current_state]} с вероятностью {probability})")

        else:
            print(f"Для сигнала {signal} в состоянии {current_state} переходов нет.")
    else:
        print(f"Сигнал {signal} не поддерживается в состоянии {current_state}")


# Цикл для ввода сигналов
while True:
    print(f"\nТекущее состояние: {current_state} ({outputs[current_state]})")
    signal = input("Введите сигнал (Включить, Температура достигнута, Охлаждение, Выключить) или 'стоп' для завершения: ")

    if signal.lower() == 'стоп':
        print("Программа завершена.")
        break

    handle_signal(signal)
