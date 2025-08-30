from data.data_utils import get_data


def find_contact(data: dict, value: str) -> list :  # ✅
    """
    Ищем контакт в обьекте - возвратим массив контактов или пустой
    """
    res = []
    for k, list_nums in data.items():
        for el in  list_nums:
            if el.find(value) != -1:
                res.append((k, el))
    return res

# Отдельная функция для печати
def find_contact_to_data(value: str):
    """
    получаем данные - ищем контакт - найден - вывод - нет пишем
    """
    data = get_data()
    res = find_contact(data, value)
    if not res:
        print('контакты с таким номером не найдены')
    else:
        print('найдено:')
        for k, v  in res:
            print(f'{k} :  {v}')


if __name__ == "__main__":
    find_contact_to_data('32')
