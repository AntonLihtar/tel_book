import pytest
from  commands.find import find_contact

def test_find_existing_contact_by_full_number():
    """Тест поиска контакта по полному номеру"""
    data = {
        "Иван": ["123-456"],
        "Мария": ["987-654"],
        "Петр": ["555-123"]
    }
    result = find_contact(data, "123-456")
    assert result == [("Иван", "123-456")]

def test_find_existing_contact_by_partial_number():
    """Тест поиска контакта по части номера"""
    data = {
        "Иван": ["123-456"],
        "Мария": ["987-654"],
        "Петр": ["555-123"]
    }
    result = find_contact(data, "123")
    expected = [("Иван", "123-456"), ("Петр", "555-123")]
    assert sorted(result) == sorted(expected)

def test_find_non_existing_contact():
    """Тест поиска несуществующего номера"""
    data = {
        "Иван": ["123-456"],
        "Мария": ["987-654"],
    }
    result = find_contact(data, "999-999")
    assert result == []

def test_find_in_empty_dict():
    """Тест поиска в пустом словаре"""
    data = {}
    result = find_contact(data, "123-456")
    assert result == []

def test_find_empty_string():
    """Тест поиска пустой строки (найдет все контакты)"""
    data = {
        "Иван": ["123-456"],
        "Мария": ["987-654"],
    }
    result = find_contact(data, "")
    expected = [("Иван", "123-456"), ("Мария", "987-654")]
    assert sorted(result) == sorted(expected)

def test_find_special_characters():
    """Тест поиска с специальными символами"""
    data = {
        "Иван": ["+7(999)123-45-67"],
        "Мария": ["8-800-555-35-35"]
    }
    result = find_contact(data, "+7")
    assert result == [("Иван", "+7(999)123-45-67")]

def test_find_multiple_matches_same_contact():
    """Тест: если номер встречается в одном контакте несколько раз"""
    data = {
        "Иван": ["123-456-123"],
        "Мария": ["987-654"]
    }
    result = find_contact(data, "123")
    assert result == [("Иван", "123-456-123")]

def test_find_case_sensitive():
    """Тест: поиск регистрозависимый"""
    data = {
        "Иван": ["ABC-123"],
        "Мария": ["abc-456"]
    }
    result = find_contact(data, "ABC")
    assert result == [("Иван", "ABC-123")]

def test_find_with_spaces():
    """Тест поиска с пробелами"""
    data = {
        "Иван": ["123 456"],
        "Мария": ["789 012"]
    }
    result = find_contact(data, "123")
    assert result == [("Иван", "123 456")]

def test_find_duplicate_numbers_different_contacts():
    """Тест: одинаковые номера у разных контактов"""
    data = {
        "Иван": ["123-456"],
        "Мария": ["123-456"],
        "Петр": ["789-012"]
    }
    result = find_contact(data, "123-456")
    expected = [("Иван", "123-456"), ("Мария", "123-456")]
    assert sorted(result) == sorted(expected)

def test_return_type_is_list_of_tuples():
    """Тест: проверка типа возвращаемого значения"""
    data = {"Иван": ["123-456"]}
    result = find_contact(data, "123")
    assert isinstance(result, list)
    if result:  # Если есть результаты
        assert isinstance(result[0], tuple)
        assert len(result[0]) == 2