import pytest

def add_contact_to_dict(data: dict, contact: str, value: str) -> dict:
    """
    Добавляем контакт в объект - если есть - расширяем номера
    """
    if contact in data:
        data[contact] = f'{data[contact]} {value}'
    else:
        data[contact] = value
    return data

def test_add_new_contact():
    """Тест добавления нового контакта"""
    data = {}
    result = add_contact_to_dict(data, "Иван", "123-456")
    assert result == {"Иван": "123-456"}

def test_add_phone_to_existing_contact():
    """Тест добавления номера к существующему контакту"""
    data = {"Иван": "123-456"}
    result = add_contact_to_dict(data, "Иван", "789-012")
    assert result == {"Иван": "123-456 789-012"}

def test_add_multiple_phones():
    """Тест добавления нескольких номеров"""
    data = {"Иван": "123-456"}
    data = add_contact_to_dict(data, "Иван", "789-012")
    result = add_contact_to_dict(data, "Иван", "345-678")
    assert result == {"Иван": "123-456 789-012 345-678"}

def test_add_contact_with_empty_dict():
    """Тест с пустым словарем"""
    data = {}
    result = add_contact_to_dict(data, "Мария", "987-654")
    assert result == {"Мария": "987-654"}

def test_add_contact_existing_empty_value():
    """Тест добавления к контакту с пустым значением"""
    data = {"Иван": ""}
    result = add_contact_to_dict(data, "Иван", "123-456")
    assert result == {"Иван": " 123-456"}  # Обратите внимание на пробел в начале

def test_add_contact_none_value():
    """Тест добавления к контакту со значением None"""
    data = {"Иван": None}
    result = add_contact_to_dict(data, "Иван", "123-456")
    assert result == {"Иван": "None 123-456"}  # str(None) = "None"

def test_empty_contact_name():
    """Тест с пустым именем контакта"""
    data = {}
    result = add_contact_to_dict(data, "", "123-456")
    assert result == {"": "123-456"}

def test_empty_phone_value():
    """Тест с пустым номером телефона"""
    data = {}
    result = add_contact_to_dict(data, "Иван", "")
    assert result == {"Иван": ""}