from collections import defaultdict

def count_finger_loads(text, keylout_jcuken, keylout_jcuken_shift, keylout_vizov, keylout_vizov_shift):
    """
    Подсчитывает нагрузку на каждый палец для всех раскладок:
    - ЙЦУКЕН
    - ВЫЗОВ
    - ЙЦУКЕН с Shift
    - ВЫЗОВ с Shift
    
    Возвращает два словаря:
    1. Нагрузку на пальцы для ЙЦУКЕН (включая Shift).
    2. Нагрузку на пальцы для ВЫЗОВ (включая Shift).
    """
    # Инициализация словарей для нагрузки на пальцы
    finger_loads_ycu = defaultdict(int)  # Нагрузка для ЙЦУКЕН
    finger_loads_vyzov = defaultdict(int)  # Нагрузка для ВЫЗОВ

    # Подсчет символов в тексте
    symbol_counts = defaultdict(int)
    for char in text:
        symbol_counts[char] += 1

    # Подсчет нагрузки для ЙЦУКЕН и ВЫЗОВ
    for finger, symbols in keylout_jcuken.items():
        for symbol in symbols:
            finger_loads_ycu[finger] += symbol_counts.get(symbol, 0)
    for finger, symbols in keylout_jcuken_shift.items():
        for symbol in symbols:
            finger_loads_ycu[finger] += symbol_counts.get(symbol, 0)

    for finger, symbols in keylout_vizov.items():
        for symbol in symbols:
            finger_loads_vyzov[finger] += symbol_counts.get(symbol, 0)
    for finger, symbols in keylout_vizov_shift.items():
        for symbol in symbols:
            finger_loads_vyzov[finger] += symbol_counts.get(symbol, 0)

    return finger_loads_ycu, finger_loads_vyzov
