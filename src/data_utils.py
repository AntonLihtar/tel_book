from pathlib import Path
import json

file_path = Path('data') / 'data.json'
if __name__ == "__main__":
    if file_path.exists():
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # ✅ Правильно
            print(data)