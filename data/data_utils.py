from pathlib import Path
import json

"""
при каждом запросе чтения - перезапускаем ф - для обновления файла json

ф: *парсер get_data()
проверяем что файл есть - читаем - парсим

чтение файла:  
Показать все контакты:
list
*парсер - выводим ключи обьекта?

чтение по ключу:  
*парсер - выводим значение по ключу?

поиск по значению 
*парсер - поиск в обьекте

"""
# Создаем путь от корня проекта (на уровень выше)
project_root = Path(__file__).parent.parent  # поднимаемся из data/ в корень


def open_read_file(f_path: str):
    """
    Возвращает обьект с данными из файла по пути до файла
    """

    f_path = project_root / f_path
    # Проверяем расширение
    if f_path.suffix != '.json':
        raise ValueError(f"Файл должен иметь расширение .json, получено: {f_path.suffix}")

    # Проверяем существование
    if not f_path.exists():
        raise FileNotFoundError(f"Файл не найден: {f_path}")

    try:
        with open(f_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Файл {f_path} содержит некорректный JSON: {e}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла {f_path}: {e}")


# Создаем путь относительно текущего файла - работает с любых способов запуска
file_path = Path(__file__).parent / 'data.json'


def get_data() -> dict:  # ✅
    """
    Возвращает обьект с данными из файла - при ошибке возвращаем пустой словарь
    """
    try:
        return open_read_file('data/data.json')  # путь по умолчанию
    except FileNotFoundError:
        print("Файл не найден, создаем новый пустой справочник")
        return {}
    except ValueError as e:
        print(f"Ошибка данных: {e}")
        return {}
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return {}


def set_data(data: dict):  # ✅
    """
    записываем данные (json обьект) в файл
    """
    try:
        # Всегда пытаемся записать файл (создастся, если не существует)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            # print('данные записаны')
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


if __name__ == "__main__":
    # print(get_data())
    print(open_read_file('data/data.json'))
    print(open_read_file('t2.json'))
    # print(open_read_file('data/t3.py'))
