"""
Вызывает функции analyze_finger_loads, plot_finger_load_comparison_horizontal
"""


from utils import load_text
from analyze import analyze_finger_loads
from plotter import plot_finger_load_comparison, plot_finger_load_comparison_horizontal
from config import keylout_dd, keylout_shift

def main():    

    # Загрузка текста из файла
    text = load_text("voina-i-mir.txt")
    
    # Анализ нагрузки на пальцы
    finger_loads_ycu, finger_loads_vyzov = analyze_finger_loads(text, keylout_dd, keylout_shift)
    
    # Построение вертикальной сравнительной гистограммы нагрузок на пальцы
    plot_finger_load_comparison(finger_loads_ycu, finger_loads_vyzov)
    
    # Построение горизонтальной сравнительной гистограммы нагрузок на пальцы
    plot_finger_load_comparison_horizontal(finger_loads_ycu, finger_loads_vyzov)

if __name__ == "__main__":
    main()
