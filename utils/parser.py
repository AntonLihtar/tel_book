"""
принимаем строку
ответ может быть 3 варианта

команда

команда + имя *фамилия

команда + имя *фамилия + номер

возвращаем
команда + параметры

"""


def parse_command(command: str) -> tuple: # ✅ + test
    command = command.strip()
    if command in ['exit', 'list']:
        return command, None

    if "'" in command:
        raise Exception("недопустимые символы")

    if '"' in command:
        elements = [el.strip() for el in command.split('"')]
        if elements[1].strip() == '':
            raise Exception("неправильные аргументы")
        elements = [el for el in elements if el.strip()]
    else:
        elements = command.split()

    if len(elements) < 2:
        raise Exception("в команде недостает аргументов")

    if len(elements) > 3:
        raise Exception("в команде слишком много аргументов")

    return elements[0], tuple(elements[1:])
