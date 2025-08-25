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


def get_data() -> dict:  # ✅
    """
    Возвращает обьект с данными из файла - при ошибке возвращаем пустой словарь
    """
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    print('файл не существует')
    return {}


def handle_list_command(params: str | None):
    data = get_data()
    if params:
        value = data.get(params[0])
        if value:
            print(f"{params[0]}: {value}")
        else:
            print('Такого контакта не существует')
    else:
        contacts = list(data.keys())
        if contacts:
            print('Все контакты:')
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact}")
        else:
            print('Контактов нет')

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
    # print('ut file_path --', file_path)
    # print(get_data())
    # print(file_path.is_absolute())
    #
    # print(set_contact_to_data('Jack', 999))

    print(handle_list_command('ss'))
