from utils import load_text
from analyze import count_finger_loads
from plotter import plot_finger_load_comparison_horizontal
from config import keylout_jcuken, keylout_jcuken_shift, keylout_vizov, keylout_vizov_shift

def main():    

    # Загрузка текста из файла
    text = load_text("voina-i-mir.txt")
    
    # Анализ нагрузки на пальцы
    finger_loads_ycu, finger_loads_vyzov = count_finger_loads(text, keylout_jcuken, keylout_jcuken_shift, keylout_vizov, keylout_vizov_shift)
    
    # Построение горизонтальной сравнительной гистограммы нагрузок на пальцы
    plot_finger_load_comparison_horizontal(finger_loads_ycu, finger_loads_vyzov)

if __name__ == "__main__":
    main()