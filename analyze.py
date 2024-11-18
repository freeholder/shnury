"""
Функции analyze_finger_loads и analyze_text_symbols
"""

from collections import defaultdict

def analyze_text_symbols(text, keylout_dd, keylout_shift):
    """
    Подсчитывает количество нажатий для каждого символа на основе текста и раскладок клавиатуры.

    Параметры:
    - text: строка текста, для которой производится подсчет частот символов.
    - keylout_dd: словарь, где ключи — названия пальцев, а значения — списки символов, доступных для каждого пальца в раскладках ЙЦУКЕН и ВЫЗОВ.
                  Каждое значение представляет собой список с двумя вложенными списками:
                  первый — символы для ЙЦУКЕН, второй — для ВЫЗОВ.
    - keylout_shift: словарь, где ключи — названия пальцев, а значения — списки символов, которые используются при зажатой клавише Shift
                     для раскладок ЙЦУКЕН и ВЫЗОВ.

    Возвращает:
    - symbol_counts: словарь, где ключи — символы, а значения — количество нажатий каждого символа на основе текста.
    """
    symbol_counts = defaultdict(int)

    # Создание множества всех символов из раскладки для быстрого поиска
    all_keys = set(key for groups in keylout_dd.values() for group in groups for key in group)
    shift_keys = set(key for groups in keylout_shift.values() for group in groups for key in group)

    # Пройтись по каждому символу текста и обновить счетчики
    for char in text:
        if char in all_keys or char in shift_keys:
            symbol_counts[char] += 1

    return symbol_counts


from collections import defaultdict


def analyze_finger_loads(text, keylout_dd, keylout_shift):
    """
    Подсчитывает нагрузку на каждый палец на основе текста и раскладок клавиатуры.

    Параметры:
    - text: строка текста, для которой производится анализ.
    - keylout_dd: словарь, где ключи — названия пальцев, а значения — списки символов, доступных для каждого пальца в раскладках ЙЦУКЕН и ВЫЗОВ.
                  Каждое значение представляет собой список с двумя вложенными списками:
                  первый — символы для ЙЦУКЕН, второй — для ВЫЗОВ.
    - keylout_shift: словарь, где ключи — названия пальцев, а значения — списки символов, которые используются при зажатой клавише Shift
                     для раскладок ЙЦУКЕН и ВЫЗОВ.

    Возвращает:
    - два словаря, где ключи — пальцы, а значения — суммарное количество нажатий для каждого пальца на основе текста:
      - finger_loads_ycu: словарь для раскладки ЙЦУКЕН
      - finger_loads_vyzov: словарь для раскладки ВЫЗОВ
    """
    finger_loads_ycu = defaultdict(int)  # Для ЙЦУКЕН
    finger_loads_vyzov = defaultdict(int)  # Для ВЫЗОВ

    # Объединение символов с их частотами
    symbol_counts = analyze_text_symbols(text, keylout_dd, keylout_shift)

    # Распределение символов по пальцам для обеих раскладок
    for finger, layouts in keylout_dd.items():
        # Если для пальца есть только одна раскладка, то добавляем пустую раскладку для второй
        if len(layouts) == 1:
            symbols_ycu = layouts[0]
            symbols_vyzov = []
        else:
            symbols_ycu, symbols_vyzov = layouts

        # Считаем частоты для каждой раскладки
        for symbol in symbols_ycu:
            finger_loads_ycu[finger] += symbol_counts.get(symbol, 0)
        for symbol in symbols_vyzov:
            finger_loads_vyzov[finger] += symbol_counts.get(symbol, 0)

    return finger_loads_ycu, finger_loads_vyzov



