"""
Функции plot_finger_load_comparison и plot_finger_load_comparison_horizontal
"""

import matplotlib.pyplot as plt

def plot_finger_load_comparison(finger_loads_ycu, finger_loads_vyzov):
    """
    Строит вертикальную сравнительную гистограмму нагрузок на каждый палец для раскладок ЙЦУКЕН и ВЫЗОВ.

    Параметры:
    - finger_loads_ycu: словарь с частотой нажатий для каждой буквы в раскладке ЙЦУКЕН.
                        Ключи - названия пальцев, значения - частота нажатий.
    - finger_loads_vyzov: словарь с частотой нажатий для каждой буквы в раскладке ВЫЗОВ.
                          Ключи - названия пальцев, значения - частота нажатий.

    Гистограмма строится в виде двух вертикальных столбцов для каждой из раскладок,
    позволяя визуально сравнить нагрузку на пальцы.
    """
    fingers = list(finger_loads_ycu.keys())
    loads_ycu = [finger_loads_ycu[finger] for finger in fingers]
    loads_vyzov = [finger_loads_vyzov[finger] for finger in fingers]

    # Построение вертикальной сравнительной гистограммы
    x = range(len(fingers))  # позиции для каждого пальца
    plt.figure(figsize=(10, 6))
    bar_width = 0.4  # ширина каждого столбца

    plt.bar(x, loads_ycu, width=bar_width, label="ЙЦУКЕН", color="skyblue", align='center')
    plt.bar([pos + bar_width for pos in x], loads_vyzov, width=bar_width, label="ВЫЗОВ", color="salmon", align='center')

    plt.xlabel("Пальцы")
    plt.ylabel("Частота нажатий")
    plt.title("Сравнительная нагрузка на пальцы для раскладок ЙЦУКЕН и ВЫЗОВ (вертикальная)")
    plt.xticks([pos + bar_width / 2 for pos in x], fingers, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_finger_load_comparison_horizontal(finger_loads_ycu, finger_loads_vyzov):
    """
    Строит горизонтальную сравнительную гистограмму нагрузок на каждый палец для раскладок ЙЦУКЕН и ВЫЗОВ.

    Параметры:
    - finger_loads_ycu: словарь с частотой нажатий для каждой буквы в раскладке ЙЦУКЕН.
                        Ключи - названия пальцев, значения - частота нажатий.
    - finger_loads_vyzov: словарь с частотой нажатий для каждой буквы в раскладке ВЫЗОВ.
                          Ключи - названия пальцев, значения - частота нажатий.

    Гистограмма строится в виде двух горизонтальных полос для каждой из раскладок,
    позволяя визуально сравнить нагрузку на пальцы.
    """
    fingers = list(finger_loads_ycu.keys())
    loads_ycu = [finger_loads_ycu[finger] for finger in fingers]
    loads_vyzov = [finger_loads_vyzov[finger] for finger in fingers]

    # Построение горизонтальной сравнительной гистограммы
    y = range(len(fingers))  # позиции для каждого пальца
    plt.figure(figsize=(10, 6))
    bar_height = 0.4  # высота каждого столбца

    plt.barh(y, loads_ycu, height=bar_height, label="ЙЦУКЕН", color="skyblue", align='center')
    plt.barh([pos + bar_height for pos in y], loads_vyzov, height=bar_height, label="ВЫЗОВ", color="salmon", align='center')

    plt.ylabel("Пальцы")
    plt.xlabel("Частота нажатий")
    plt.title("Сравнительная нагрузка на пальцы для раскладок ЙЦУКЕН и ВЫЗОВ (горизонтальная)")
    plt.yticks([pos + bar_height / 2 for pos in y], fingers)
    plt.legend()
    plt.tight_layout()
    plt.show()
