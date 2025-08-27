from data.data_utils import get_data, set_data


def delete_contact_to_dict(data: dict, contact:str) -> dict:  # ✅
    """
    Удаляем контакт из словаря
    """
    if contact in data:
        del data[contact]
        print(f'контакт "{contact}" удален')
    else:
        print(f'контакта "{contact}" нет в словаре')
    return data

# Отдельная функция для печати
def delete_contact_to_data(contact:str):
    """
    получаем данные - Удаляем контакт и добавляем данные в файл
    """
    data = get_data()
    data = delete_contact_to_dict(data, contact)
    set_data(data)

if __name__ == "__main__":
    # delete_contact_to_data('test')
    print(delete_contact_to_dict({'a': 1, 'b':2}, 'b'))