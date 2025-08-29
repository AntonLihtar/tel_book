from data.data_utils import get_data, set_data, open_read_file

"""
читаем основной файл - получаем данные
читаем доп - получаем данные 
чекаем
"""


def merge_dicts(data: dict, new_data: dict) -> dict:  # ✅
    """
    обьединяем 2 обьекта
    """
    # for el in new_data:
    #     if el in data:


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
    data =
    set_data(data)

if __name__ == "__main__":
    add_contact_to_data('test', '123')
