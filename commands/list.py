from data.data_utils import get_data


def handle_list_command(data: dict, params: str | None) -> str:
    """
    Обрабатывает команду list и возвращает результат как строку
    """
    if params:
        contact_name = params[0]
        value = data.get(contact_name)
        if value:
            return f"{contact_name}: {value}"
        else:
            return 'Такого контакта не существует'
    else:
        contacts = list(data.keys())
        if contacts:
            result = ['Все контакты:']
            for i, contact in enumerate(contacts, 1):
                result.append(f"{i}. {contact}")
            return '\n'.join(result)
        else:
            return 'Контактов нет'


# Отдельная функция для печати
def print_list_command(params: str | None):
    data = get_data()
    """Печатает результат handle_list_command"""
    result = handle_list_command(data, params)
    print(result)


if __name__ == "__main__":
    print(print_list_command(('anton',)))
