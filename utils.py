def load_text(filename):
    """
    Загружает текст из файла и возвращает его в виде строки.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
