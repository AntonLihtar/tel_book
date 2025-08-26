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

# Создаем путь относительно текущего файла - работает с любых способов запуска
file_path = Path(__file__).parent / 'data.json'


def get_data() -> dict:  # ✅
    """
    Возвращает обьект с данными из файла - при ошибке возвращаем пустой словарь
    """
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    print('файл не существует')
    return {}


def set_contact_to_data(contact, value) -> bool:  # ✅
    """
    Добавляем контакт в данные
    """
    data = get_data()
    data[contact] = str(value)

    try:
        # Всегда пытаемся записать файл (создастся, если не существует)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return True
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")
        return False

if __name__ == "__main__":
        print(get_data())
