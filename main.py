from utils.parser import parse_command
from commands.list import print_list_command
from commands.add import add_contact_to_data
from commands.delete import delete_contact_to_data
from commands.find import find_contact_to_data


def while_program():
    while True:
        try:
            user_input = input("Enter command: ").strip()

            if not user_input:
                continue

            command, param = parse_command(user_input)  # ✅ + test
            print(f"Command name = {command}, command_param = {param}")

            if command == "exit":  # ✅
                print("Программа завершена")
                break

            elif command == "list": # ✅ + test
                print_list_command(param)

            elif command == "add": # ✅ + test
                if len(param) == 2:
                    add_contact_to_data(*param)
                else:
                    raise Exception("команда 'add' требует 2 аргумента")

            elif command == "find":
                if len(param) == 1:
                    find_contact_to_data(param[0])
                else:
                    raise Exception("команда 'find' требует 1 аргумент")

            elif command == "merge":  # ✅ + test
                pass

            elif command == "delete":
                delete_contact_to_data(param[0])

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
