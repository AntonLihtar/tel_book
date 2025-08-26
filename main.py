from utils.parser import parse_command
from commands.list import print_list_command
from commands.add import add_contact_to_data


def while_program():
    while True:
        try:
            user_input = input("Enter command: ").strip()

            if not user_input:
                continue

            command, param = parse_command(user_input) # ✅ + test
            print(f"Command name = {command}, command_param = {param}")

            if command == "exit": # ✅
                print("Программа завершена")
                break

            elif command == "list":
                print_list_command(param) # ✅ + test

            elif command == "add":
                if len(param) == 2:
                    add_contact_to_data(*param)
                else:
                    raise Exception("команда 'add' требует 2 аргумента")

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
