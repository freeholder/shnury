def load_text(filename):
    """
    Загружает текст из файла и возвращает его содержимое.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def load_lexemes(filename):
    """
    Загружает лексемы из файла. Каждая строка считается одной лексемой.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
