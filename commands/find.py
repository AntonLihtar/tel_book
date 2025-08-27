from data.data_utils import get_data, set_data


def find_contact(data: dict, contact:str, value:str) -> dict:  # ✅
    """
    Добавляем контакт в обьект - если есть - расширяем номера
    """
    if contact in data:
        if value in data[contact]:
            raise Exception("такой номером уже существует у контакта")
        data[contact].append(value)
        print(f'контакту "{contact}" добавлен номер "{value}"')

    else:
        data[contact] = [value]
        print(f'контакт "{contact}" с номером "{value}" добавлен')
    return data

# Отдельная функция для печати
def find_contact_to_data(contact:str, value:str):
    """
    получаем данные - ищем контакт - найден - вывод - нет пишем
    """
    data = get_data()
    data = add_contact_to_dict(data, contact, value)

if __name__ == "__main__":
    add_contact_to_data('test', '123')
