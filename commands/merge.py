from data.data_utils import get_data, set_data, open_read_file
from commands.add import add_contact_to_dict

"""
читаем основной файл - получаем данные
читаем доп - получаем данные 
чекаем
"""


def merge_dicts(data: dict, new_data: dict) -> dict:  # ✅
    """
    обьединяем 2 обьекта
    """
    for key, value in new_data.items():
        print(f'ele {key} {value}')
        for number in value:
            try:
                data = add_contact_to_dict(data, key, number)
            except Exception as e:
                print(f"Ошибка добавления:{number} в {key} {e}")
    return data


# Отдельная функция для печати
def merge_contacts(path: str):
    """
    получаем ссылку - открываем - получаем данные
    повторяем со 2рым файлом
    отправляем на слияние обьектов
    """
    dop_data = open_read_file(path)
    data = get_data()
    data = merge_dicts(data, dop_data)
    set_data(data)


if __name__ == "__main__":
    merge_contacts('t2.json')
