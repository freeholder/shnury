import matplotlib.pyplot as plt

def plot_finger_load_comparison_horizontal(finger_loads, layout_names):
    """
    Строит горизонтальную сравнительную гистограмму нагрузок на пальцы для всех раскладок.
    :param finger_loads: список словарей с нагрузкой на пальцы.
    :param layout_names: названия раскладок.
    """
    # Индекс для "ЙЦУКЕН", чтобы всегда сделать его первым
    jcuken_index = layout_names.index("ЙЦУКЕН")

    # Перемещаем "ЙЦУКЕН" в начало списка
    finger_loads = [finger_loads[jcuken_index]] + [finger_loads[i] for i in range(len(finger_loads)) if i != jcuken_index]
    layout_names = [layout_names[jcuken_index]] + [layout_names[i] for i in range(len(layout_names)) if i != jcuken_index]
    
    num_layouts = len(finger_loads)
    fingers = list(finger_loads[0].keys())  # Список пальцев
    y_positions = range(len(fingers))  # Позиции для пальцев

    plt.figure(figsize=(12, 10))
    bar_height = 0.15  # Высота столбцов

    # Построение горизонтальных гистограмм
    for i, (loads, name) in enumerate(zip(finger_loads, layout_names)):
        values = [loads[finger] for finger in fingers]
        plt.barh(
            [y + i * bar_height for y in y_positions], 
            values, 
            height=bar_height, 
            label=name
        )
    
    # Настройка графика
    plt.ylabel("Пальцы")
    plt.xlabel("Частота нажатий")
    plt.title("Сравнительная нагрузка на пальцы для раскладок (горизонтальная)")
    
    # Подписи оси Y: Указываем пальцы по центру всех раскладок
    plt.yticks(
        [y + bar_height * (num_layouts - 1) / 2 for y in y_positions], 
        fingers
    )
    
    # Легенда
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()
