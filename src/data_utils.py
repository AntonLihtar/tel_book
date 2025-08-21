from pathlib import Path
import json

"""
при каждом запросе чтения - перезапускаем ф - для обновления файла json

ф: *парсер get_data()
проверяем что файл есть - читаем - парсим

чтение файла:  
Показать все контакты:
list
*парсер - выводим ключи обьекта?

чтение по ключу:  
*парсер - выводим значение по ключу?

поиск по значению 
*парсер - поиск в обьекте

"""

file_path = Path('data') / 'data.json'


def get_data() -> dict | None:
    if file_path.exists():
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def get_contacts() -> list | None:
    data = get_data()
    if data:
        return list(data.keys())
    return None


if __name__ == "__main__":
    print('ut')
    print(get_data())
    print(get_contacts())
