import pytest
from commands.merge import merge_dicts


def test_merge_two_simple_dicts():
    """Тест объединения двух простых словарей без пересечений"""
    data1 = {"Иван": ["123-456"]}
    data2 = {"Мария": ["987-654"]}

    result = merge_dicts(data1, data2)
    expected = {"Иван": ["123-456"], "Мария": ["987-654"]}
    assert result == expected


def test_merge_with_existing_contact_different_numbers():
    """Тест объединения с существующим контактом и разными номерами"""
    data1 = {"Иван": ["123-456"]}
    data2 = {"Иван": ["789-012"], "Мария": ["987-654"]}

    result = merge_dicts(data1, data2)
    expected = {"Иван": ["123-456", "789-012"], "Мария": ["987-654"]}
    assert result == expected


def test_merge_with_duplicate_numbers():
    """Тест объединения с дубликатами номеров"""
    data1 = {"Иван": ["123-456"]}
    data2 = {"Иван": ["123-456"], "Мария": ["987-654"]}

    result = merge_dicts(data1, data2)
    # Дубликат не должен добавиться
    expected = {"Иван": ["123-456"], "Мария": ["987-654"]}
    assert result == expected


def test_merge_empty_dicts():
    """Тест объединения пустых словарей"""
    data1 = {}
    data2 = {}

    result = merge_dicts(data1, data2)
    assert result == {}


def test_merge_with_empty_source_dict():
    """Тест объединения пустого исходного словаря"""
    data1 = {}
    data2 = {"Иван": ["123-456"], "Мария": ["987-654"]}

    result = merge_dicts(data1, data2)
    assert result == {"Иван": ["123-456"], "Мария": ["987-654"]}


def test_merge_with_empty_new_dict():
    """Тест объединения с пустым новым словарем"""
    data1 = {"Иван": ["123-456"]}
    data2 = {}

    result = merge_dicts(data1, data2)
    assert result == {"Иван": ["123-456"]}


def test_merge_multiple_numbers_per_contact():
    """Тест объединения с несколькими номерами у контактов"""
    data1 = {"Иван": ["123-456", "111-111"]}
    data2 = {"Иван": ["789-012", "222-222"], "Мария": ["987-654", "333-333"]}

    result = merge_dicts(data1, data2)
    expected = {
        "Иван": ["123-456", "111-111", "789-012", "222-222"],
        "Мария": ["987-654", "333-333"]
    }
    assert result == expected


def test_merge_contacts_with_special_characters():
    """Тест объединения контактов со специальными символами"""
    data1 = {"Иван Петров": ["+7(123)456"]}
    data2 = {"Иван Петров": ["+7(789)012"], "Мария@компания": ["987-654"]}

    result = merge_dicts(data1, data2)
    expected = {
        "Иван Петров": ["+7(123)456", "+7(789)012"],
        "Мария@компания": ["987-654"]
    }
    assert result == expected


def test_merge_with_empty_strings():
    """Тест объединения с пустыми строками"""
    data1 = {"Иван": ["123-456"]}
    data2 = {"": [""], "Иван": [""]}

    result = merge_dicts(data1, data2)
    expected = {"Иван": ["123-456", ""], "": [""]}
    assert result == expected


def test_merge_same_contact_multiple_duplicates():
    """Тест: несколько дубликатов одного номера"""
    data1 = {"Иван": ["123-456", "789-012"]}
    data2 = {"Иван": ["123-456", "789-012", "555-123"]}

    result = merge_dicts(data1, data2)
    # Только новый номер должен добавиться
    expected = {"Иван": ["123-456", "789-012", "555-123"]}
    assert result == expected