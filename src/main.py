from utils import parse_command

if __name__ == "__main__":

    cmd_name: str = ''
    # while cmd_name != "exit":
    # todo: убрать после тестов
    while cmd_name != '1':
        # cmd_name = input("Enter command: ")
        # todo: убрать после тестов
        cmd_name = 'list "Asik Ssort" +79210008832'
        command_name, command_param = parse_command(cmd_name)
        if command_name == "list":
            pass
        elif command_name == "new":
            pass
        else:
            print("Unknown commad")
        print(
            f"Command name = {command_name}, command_param = {command_param}")

        # todo: убрать после тестов
        cmd_name = '1'
