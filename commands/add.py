from data.data_utils import get_data, set_data


def add_contact_to_dict(data: dict, contact:str, value:str) -> dict:  # ✅
    """
    Добавляем контакт в обьект - если есть - расширяем номера
    """
    if contact in data:
        if value in data[contact]:
            raise Exception("такой контакт уже существует")
        else:
            data[contact].append(value)
            print(f'для контакта "{contact}" добавили номер "{value}"')
    else:
        data[contact] = [value]
        print(f'контакт "{contact}" с номером "{value}" добавлен')
    return data

# Отдельная функция для печати
def add_contact_to_data(contact:str, value:str):
    """
    получаем данные - добавляем контакт и добавляем данные в файл
    """
    data = get_data()
    data = add_contact_to_dict(data, contact, value)
    set_data(data)

if __name__ == "__main__":
    add_contact_to_data('test', '123')

    o = {'a':1,  'b':2}
    o2 = add_contact_to_dict(o, 'c', '3')
    print(o2)
    print(o==o2)
