def parse_command(command: str) -> tuple:
    if command == 'exit':
        return 'exit', ('',)

    if '"' in command:
        elements = [el.strip() for el in command.split('"')]
        if elements[1].strip() == '':
            raise Exception("2рой аргумент - пустая строка / неправильный аргумент")
        elements = [el for el in elements if el.strip()]
    else:
        elements = command.split()

    if len(elements) < 2:
        raise Exception("в команде недостает аргументов")

    return elements[0], tuple(elements[1:])
