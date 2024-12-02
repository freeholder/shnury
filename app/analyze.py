from collections import defaultdict

def count_finger_loads(text, *layouts):
    """
    Подсчитывает нагрузку на каждый палец для всех переданных раскладок.
    :param text: текст для анализа.
    :param layouts: последовательность словарей (обычная раскладка + раскладка с Shift).
    :return: список словарей с нагрузкой на пальцы для каждой раскладки.
    """
    # Подсчет частоты символов в тексте
    symbol_counts = defaultdict(int)
    for char in text:
        symbol_counts[char] += 1

    # Подсчет нагрузки для каждой раскладки
    finger_loads = []
    for i in range(0, len(layouts), 2):  # Итерируем по парам: обычная раскладка + Shift
        layout = layouts[i]
        layout_shift = layouts[i + 1]

        # Словарь нагрузки для текущей раскладки
        current_load = defaultdict(int)

        # Учет символов обычной раскладки
        for finger, symbols in layout.items():
            for symbol in (symbols if isinstance(symbols, (list, tuple, set)) else [symbols]):
                current_load[finger] += symbol_counts.get(symbol, 0)
        
        # Учет символов раскладки с Shift
        for finger, symbols in layout_shift.items():
            for symbol in (symbols if isinstance(symbols, (list, tuple, set)) else [symbols]):
                current_load[finger] += symbol_counts.get(symbol, 0)

        # Добавляем результаты для текущей раскладки
        finger_loads.append(current_load)
    
    return finger_loads
