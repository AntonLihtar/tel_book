import pytest
from commands.add import add_contact_to_dict


def test_add_new_contact():
    """Тест добавления нового контакта"""
    data = {}
    result = add_contact_to_dict(data, "Иван", "123-456")
    assert result == {"Иван": ["123-456"]}


def test_add_second_phone_to_existing_contact():
    """Тест добавления второго номера к существующему контакту"""
    data = {"Иван": ["123-456"]}
    result = add_contact_to_dict(data, "Иван", "789-012")
    assert result == {"Иван": ["123-456", "789-012"]}


def test_add_duplicate_phone_raises_exception():
    """Тест: попытка добавить дубликат номера вызывает исключение"""
    data = {"Иван": ["123-456"]}

    with pytest.raises(Exception, match="такой контакт уже существует"):
        add_contact_to_dict(data, "Иван", "123-456")


def test_add_contact_empty_dict():
    """Тест добавления контакта в пустой словарь"""
    data = {}
    result = add_contact_to_dict(data, "Мария", "987-654")
    assert result == {"Мария": ["987-654"]}


def test_add_contact_with_empty_name():
    """Тест добавления контакта с пустым именем"""
    data = {}
    result = add_contact_to_dict(data, "", "123-456")
    assert result == {"": ["123-456"]}


def test_add_contact_with_empty_number():
    """Тест добавления контакта с пустым номером"""
    data = {}
    result = add_contact_to_dict(data, "Иван", "")
    assert result == {"Иван": [""]}


def test_add_empty_number_to_existing_contact():
    """Тест добавления пустого номера к существующему контакту"""
    data = {"Иван": ["123-456"]}
    result = add_contact_to_dict(data, "Иван", "")
    assert result == {"Иван": ["123-456", ""]}


def test_multiple_phones_for_same_contact():
    """Тест добавления нескольких номеров одному контакту"""
    data = {}
    data = add_contact_to_dict(data, "Иван", "123-456")
    data = add_contact_to_dict(data, "Иван", "789-012")
    result = add_contact_to_dict(data, "Иван", "555-123")

    assert result == {"Иван": ["123-456", "789-012", "555-123"]}


def test_same_phone_different_contacts():
    """Тест: один и тот же номер у разных контактов (разрешено)"""
    data = {"Иван": ["123-456"]}
    result = add_contact_to_dict(data, "Мария", "123-456")
    assert result == {"Иван": ["123-456"], "Мария": ["123-456"]}


def test_add_duplicate_in_multiple_numbers():
    """Тест: попытка добавить дубликат в список с несколькими номерами"""
    data = {"Иван": ["123-456", "789-012"]}

    with pytest.raises(Exception, match="такой контакт уже существует"):
        add_contact_to_dict(data, "Иван", "123-456")


def test_contact_special_characters():
    """Тест: контакт со специальными символами"""
    data = {}
    result = add_contact_to_dict(data, "Иван Петров", "+7(999)123-45-67")
    assert result == {"Иван Петров": ["+7(999)123-45-67"]}


def test_multiple_different_contacts():
    """Тест работы с несколькими разными контактами"""
    data = {"Иван": ["123-456"]}
    result = add_contact_to_dict(data, "Мария", "987-654")
    assert result == {"Иван": ["123-456"], "Мария": ["987-654"]}