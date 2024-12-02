import pytest
from collections import defaultdict
from app.analyze import count_finger_loads  # Замените на реальный путь импорта

# Ваши раскладки
keylout_jcuken = {
    'lfi5': ('ё', '1', 'й', 'ф', 'я'),
    'lfi4': ('2', 'ц', 'ы', 'ч'),
    'lfi3': ('3', 'у', 'в', 'с'),
    'lfi2': ('4', 'к', 'а', 'м', '5', 'е', 'п', 'и'),
    'lfi1': (' '),
    'rfi2': ('6', 'н', 'р', 'т', '7', 'г', 'о', 'ь'),
    'rfi3': ('8', 'ш', 'л', 'б'),
    'rfi4': ('9', 'щ', 'д', 'ю'),
    'rfi5': ('0', 'з', 'ж', '?', '-', 'х', 'э', '=', 'ъ', '\\')
}

keylout_jcuken_shift = {
    'lfi5': ('~', '!'),
    'lfi4': ('@'),
    'lfi3': ('#'),
    'lfi2': ('$', '%'),
    'rfi2': ('^', '&'),
    'rfi3': ('*'),
    'rfi4': ('('),
    'rfi5': (')', '_', '+')
}

keylout_vizov = {
    'lfi5': ('$', '%', 'б', 'ч', 'ш'),
    'lfi4': ('[', 'ы', 'и', 'х'),
    'lfi3': ('{', 'о', 'е'),
    'lfi2': ('}', '(', 'у', 'а', 'ь', ','),
    'lfi1': (' ', '_', 'к', 'й'),
    'rfi2': ('=', 'ё', '.', '/', '*', '^', 'н', 'р'),
    'rfi3': (')', 'д', 'т', 'м'),
    'rfi4': ('+', 'я', 'с', 'ф'),
    'rfi5': (']', 'г', 'в', 'п', '!', 'ж', 'з', 'щ', 'ц', 'ъ')
}

keylout_vizov_shift = {
    'lfi5': ('$','%'),
    'lfi4': ('7'),
    'lfi3': ('5'),
    'lfi2': ('3','1'),
    'rfi2': ('9','0'),
    'rfi3': ('2'),
    'rfi4': ('4'),
    'rfi5': ('6', '8', '#')
}

# Тестовый текст
test_text = "ё123ё 4567"

def test_count_finger_loads():
    # Получаем нагрузку для раскладок
    finger_loads_ycu, finger_loads_vyzov = count_finger_loads(
        test_text, keylout_jcuken, keylout_jcuken_shift, keylout_vizov, keylout_vizov_shift
    )

    # Проверяем, что нагрузка на пальцы подсчитана корректно для ЙЦУКЕН
    assert finger_loads_ycu['lfi5'] == 3  # символ 'ё'
    assert finger_loads_ycu['lfi2'] == 2  # символы '4', '5'
    assert finger_loads_ycu['rfi5'] == 0  # символ '7'

    # Проверяем нагрузку для ВЫЗОВ
    assert finger_loads_vyzov['lfi5'] == 0  # символ '%'
    assert finger_loads_vyzov['lfi2'] == 2  # символ '6'
    assert finger_loads_vyzov['rfi5'] == 1  # символ '7'

def test_empty_text():
    # Если текст пустой, то все нагрузки должны быть равны 0
    empty_text = ""
    finger_loads_ycu, finger_loads_vyzov = count_finger_loads(
        empty_text, keylout_jcuken, keylout_jcuken_shift, keylout_vizov, keylout_vizov_shift
    )

    # Проверяем, что все пальцы не нагружены
    for finger in keylout_jcuken.keys():
        assert finger_loads_ycu[finger] == 0
    for finger in keylout_vizov.keys():
        assert finger_loads_vyzov[finger] == 0

def test_no_matching_symbols():
    # Если в тексте нет символов, которые есть в раскладке, нагрузка должна быть 0
    no_matching_text = "xyz"  # символы, которых нет в нашем тесте
    finger_loads_ycu, finger_loads_vyzov = count_finger_loads(
        no_matching_text, keylout_jcuken, keylout_jcuken_shift, keylout_vizov, keylout_vizov_shift
    )

    # Проверяем, что нагрузка на пальцы для обоих раскладок 0
    for finger in keylout_jcuken.keys():
        assert finger_loads_ycu[finger] == 0
    for finger in keylout_vizov.keys():
        assert finger_loads_vyzov[finger] == 0
