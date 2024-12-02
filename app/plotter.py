import matplotlib.pyplot as plt

def plot_finger_load_comparison_horizontal(finger_loads_ycu, finger_loads_vyzov):
    """
    Строит горизонтальную сравнительную гистограмму нагрузок на каждый палец для раскладок ВЫЗОВ (сверху) и ЙЦУКЕН (снизу).
    Также отображает разницу в нагрузке (в процентах) рядом с гистограммами.
    """
    fingers = list(finger_loads_ycu.keys())  # Список пальцев
    loads_ycu = [finger_loads_ycu[finger] for finger in fingers]
    loads_vyzov = [finger_loads_vyzov[finger] for finger in fingers]
    
    # Вычисление разницы в нагрузке (в процентах)
    differences = []
    for ycu, vyzov in zip(loads_ycu, loads_vyzov):
        if ycu == 0:  # Избегаем деления на ноль
            differences.append(0)
        else:
            diff = (vyzov - ycu) / ycu * 100
            differences.append(diff)
    
    # Построение графика
    plt.figure(figsize=(12, 8))
    bar_height = 0.4  # Высота каждого столбца
    
    # Позиции на оси Y
    y_positions = range(len(fingers))
    
    # Сначала рисуем ВЫЗОВ, затем ЙЦУКЕН
    plt.barh(y_positions, loads_vyzov, height=bar_height, label="ВЫЗОВ", color="salmon", align='center')
    plt.barh([pos + bar_height for pos in y_positions], loads_ycu, height=bar_height, label="ЙЦУКЕН", color="skyblue", align='center')
    
    # Отображение процентной разницы рядом с гистограммами ВЫЗОВ
    for i, (y_pos, diff) in enumerate(zip(y_positions, differences)):
        plt.text(loads_ycu[i] + 10, y_pos + bar_height / 2, f"{diff:+.1f}%", va='center', color='black')
    
    # Настройка осей
    plt.ylabel("Пальцы")
    plt.xlabel("Частота нажатий")
    plt.title("Сравнительная нагрузка на пальцы для раскладок ВЫЗОВ и ЙЦУКЕН (горизонтальная)")
    plt.yticks([pos + bar_height / 2 for pos in y_positions], fingers)
    plt.legend()
    plt.tight_layout()
    plt.show()
