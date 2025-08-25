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


def get_data() -> dict: # ✅
    """
    Возвращает обьект с данными из файла - при ошибке возвращаем пустой словарь
    """
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    print('файл не существует')
    return {}


def get_contacts() -> list: # ✅
    """
    Возвращает список ключей
    """
    data = get_data()
    return list(data.keys())


def get_contact(name: str) -> str | None:
    """
    Возвращает номер по имени или None
    """
    data = get_data()
    return data.get(name)


def print_contacts(): # ✅
    """
    Выводим ключи списка
    """
    keys_list = get_contacts()
    if len(keys_list) == 0:
        print('словарь пуст')
        return
    for i, contact in enumerate(keys_list, 1):
        print(f"{i}. {contact}")


def set_contact_to_data(contact, value) -> bool: # ✅
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
    # print('ut file_path --', file_path)
    # print(get_data())
    # print(file_path.is_absolute())
    #
    # print(set_contact_to_data('Jack', 999))

    print(get_contact('ss'))
