from commands.parser import parse_command
from commands.list import print_list_command


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
                print_list_command(param)

            elif command == "add":
                print('24 ', *param)
                # print('add', set_contact_to_data(*param))

            else:
                print(f"Неизвестная команда: {command}")

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break

        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":

    while_program()
    # while_program2()
