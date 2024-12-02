"""
Вызывает функции load_text, load_lexemes, count_finger_loads, plot_finger_load_comparison_horizontal
"""

from utils import load_text, load_lexemes
from analyze import count_finger_loads
from plotter import plot_finger_load_comparison_horizontal
from config import (
    keylout_jcuken, keylout_jcuken_shift,
    keylout_vizov, keylout_vizov_shift,
    layout_zubachev, layout_zubachev_shift,
    keylout_diktor, keylout_diktor_shift
)
import os

def main():
    # Проверяем пути
    text_path = "/home/true_jatu/lab1plusplus/Project/voina-i-mir.txt"
    lexemes_path = "/home/true_jatu/lab1plusplus/Project/1grams-3.txt"

    # Загрузка текста и лексем
    text = load_text(text_path)
    lexemes = load_lexemes(lexemes_path)

    # Объединяем текст и лексемы
    combined_text = text + ''.join(lexemes)
    
    # Анализ нагрузок для всех раскладок
    layouts = [
        keylout_jcuken, keylout_jcuken_shift,
        keylout_vizov, keylout_vizov_shift,
        layout_zubachev, layout_zubachev_shift,
        keylout_diktor, keylout_diktor_shift
    ]
    layout_names = [
        "ЙЦУКЕН", "ВЫЗОВ", "Зубачев", "Диктор"
    ]
    finger_loads = count_finger_loads(combined_text, *layouts)

    # Построение графиков
    plot_finger_load_comparison_horizontal(finger_loads, layout_names)

if __name__ == "__main__":
    main()
