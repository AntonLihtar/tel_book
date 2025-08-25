from utils import parse_command
from data_utils import set_contact_to_data, get_contacts, print_contacts, get_contact

if __name__ == "__main__":

    def while_program():
        cmd_name: str = ''
        while cmd_name != "exit":
            # try:
            cmd_name = input("Enter command: ")
            command_name, command_param = parse_command(cmd_name)
            print(f"Command name = {command_name}, command_param = {command_param}")

            if command_name == "list":
                if command_param:
                    value = get_contact(command_param[0])
                    print(value or 'Такого контакта не существует')
                else:
                    print('Показать все контакты:')
                    print(get_contacts())  # посмотреть массив ключей
                # print_contacts() # вывести в столбец ключи

            elif command_name == "add":
                print('24 ', *command_param)
                set_contact_to_data(*command_param)

            elif command_name == "exit":
                print("exit program")
            else:
                print("Unknown command")

        # except Exception as e:
        #     print(f"Ошибка: {e}")


    def while_program2():
        tests = [
            'list "john Smit" +79210008832',
            'add bill +79210008832',
            'delete "Albion Online"',
            'delete Thor',
            # 'delete ',
        ]

        for el in tests:
            command_name, command_param = parse_command(el)
            if command_name == "list":
                pass
            elif command_name == "new":
                pass
            else:
                print("Unknown command")
            print(
                f"Command name = {command_name}, command_param = {command_param}")


    while_program()
    # while_program2()
