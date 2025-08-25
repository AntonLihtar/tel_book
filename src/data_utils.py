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


# todo: убрать
def get_contacts() -> list | None:
    """
    Возвращает список ключей
    """
    data_dict = get_data()
    return list(data_dict.keys())


def get_contact(name: str) -> str | None:
    """
    Возвращает номер по имени или None
    """
    data_dict = get_data()
    return data_dict.get(name)


def print_contacts():
    """
    Выводим ключи списка
    """
    data_list = get_contacts()
    for x in data_list:
        print(x)


def set_contact_to_data(contact, value) -> bool:
    """
    добавим ключ
    """
    data = get_data() | {}  # получаем дату

    data[contact] = str(value)

    if file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return True
    return False


if __name__ == "__main__":
    # print('ut file_path --', file_path)
    # print(get_data())
    # print(file_path.is_absolute())
    #
    # print(set_contact_to_data('Jack', 999))

    print(get_contact('ss'))
