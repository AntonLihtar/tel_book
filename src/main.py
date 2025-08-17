from utils import parse_command

if __name__ == "__main__":

    cmd_name: str = ''

    tests = [
        'list "john Smit" +79210008832',
        'add bill +79210008832',
        'delete "Albion Online"',
        'delete Thor',
    ]
    # while cmd_name != "exit":
    # todo: убрать после тестов
    for el in tests:
        # cmd_name = input("Enter command: ")
        # todo: убрать после тестов
        command_name, command_param = parse_command(el)
        # command_name, command_param = parse_command(cmd_name)
        if command_name == "list":
            pass
        elif command_name == "new":
            pass
        else:
            print("Unknown command")
        print(
            f"Command name = {command_name}, command_param = {command_param}")

        # todo: убрать после тестов
        cmd_name = '1'
