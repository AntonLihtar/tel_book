import pytest
from commands.delete import delete_contact_to_dict

def test_delete_existing_contact():
    """Тест удаления существующего контакта"""
    data = {"Иван": "123-456", "Мария": "987-654"}
    result = delete_contact_to_dict(data, "Иван")
    assert "Иван" not in result
    assert result == {"Мария": "987-654"}

def test_delete_non_existing_contact():
    """Тест удаления несуществующего контакта"""
    data = {"Иван": "123-456"}
    result = delete_contact_to_dict(data, "Петр")
    assert result == {"Иван": "123-456"}

def test_delete_from_empty_dict():
    """Тест удаления из пустого словаря"""
    data = {}
    result = delete_contact_to_dict(data, "Иван")
    assert result == {}