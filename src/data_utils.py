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
    """
    Возвращает обьект с данными из файла
    """
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


# todo: убрать
def get_contacts(data_dict) -> list | None:
    """
    Возвращает список ключей
    """
    return list(data_dict.keys())


# todo: убрать
def print_contacts(data_list) -> None:
    """
    Выводим ключи списка
    """
    for x in data_list:
        print(x)


def set_contact_to_data(contact, value) -> bool:
    """
    добавим ключ
    """
    data = get_data()  # получаем дату
    if data is None:
        data = {}

    data[contact] = value

    if file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return True
    return False


if __name__ == "__main__":
    print('ut file_path --', file_path)
    print(get_data())
    print(file_path.is_absolute())

    print(set_contact_to_data('Jack', 999))
    print(set_contact_to_data('Igor', 8787878))
