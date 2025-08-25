from utils import parse_command
from data_utils import set_contact_to_data, handle_list_command


def while_program():
    while True:
        try:
            user_input = input("Enter command: ").strip()

            if not user_input:
                continue

            command, param = parse_command(user_input)
            print(f"Command name = {command}, command_param = {param}")

            if command == "exit":
                print("Программа завершена")
                break

            elif command == "list":
                handle_list_command(param)

            elif command == "add":
                print('24 ', *param)
                print('add', set_contact_to_data(*param))

            else:
                print(f"Неизвестная команда: {command}")

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break

        except Exception as e:
            print(f"Ошибка: {e}")


# def while_program2():
#     tests = [
#         'list "john Smit" +79210008832',
#         'add bill +79210008832',
#         'delete "Albion Online"',
#         'delete Thor',
#         # 'delete ',
#     ]
#
#     for el in tests:
#         command_name, command_param = parse_command(el)
#         if command_name == "list":
#             pass
#         elif command_name == "new":
#             pass
#         else:
#             print("Unknown command")
#         print(
#             f"Command name = {command_name}, command_param = {command_param}")


if __name__ == "__main__":

    while_program()
    # while_program2()
