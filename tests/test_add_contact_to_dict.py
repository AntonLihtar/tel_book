import pytest


def add_contact_to_dict(data: dict, contact: str, value: str) -> dict:
    """
    Добавляем контакт в объект - если есть - заменяем номер
    """
    if contact in data:
        if value == data[contact]:
            raise Exception("такой контакт уже существует")
        else:
            print(f'для контакта "{contact}" заменили номер на "{value}"')
    data[contact] = value
    print(f'контакт "{contact}" с номером "{value}" добавлен')
    return data


def test_add_new_contact():
    """Тест добавления нового контакта"""
    data = {}
    result = add_contact_to_dict(data, "Иван", "123-456")
    assert result == {"Иван": "123-456"}


def test_replace_existing_contact_number():
    """Тест замены номера у существующего контакта"""
    data = {"Иван": "123-456"}
    result = add_contact_to_dict(data, "Иван", "789-012")
    assert result == {"Иван": "789-012"}


def test_add_contact_with_same_number_raises_exception():
    """Тест попытки добавления контакта с тем же номером вызывает исключение"""
    data = {"Иван": "123-456"}

    with pytest.raises(Exception, match="такой контакт уже существует"):
        add_contact_to_dict(data, "Иван", "123-456")


def test_add_contact_with_empty_dict():
    """Тест добавления контакта в пустой словарь"""
    data = {}
    result = add_contact_to_dict(data, "Мария", "987-654")
    assert result == {"Мария": "987-654"}


def test_replace_empty_value():
    """Тест замены пустого значения"""
    data = {"Иван": ""}
    result = add_contact_to_dict(data, "Иван", "123-456")
    assert result == {"Иван": "123-456"}


def test_add_contact_with_empty_name():
    """Тест добавления контакта с пустым именем"""
    data = {}
    result = add_contact_to_dict(data, "", "123-456")
    assert result == {"": "123-456"}


def test_add_contact_with_empty_number():
    """Тест добавления контакта с пустым номером"""
    data = {}
    result = add_contact_to_dict(data, "Иван", "")
    assert result == {"Иван": ""}


def test_replace_contact_with_empty_number():
    """Тест замены номера на пустой"""
    data = {"Иван": "123-456"}
    result = add_contact_to_dict(data, "Иван", "")
    assert result == {"Иван": ""}


def test_multiple_different_contacts():
    """Тест работы с несколькими разными контактами"""
    data = {"Иван": "123-456", "Мария": "987-654"}
    result = add_contact_to_dict(data, "Петр", "555-123")
    assert result == {"Иван": "123-456", "Мария": "987-654", "Петр": "555-123"}


def test_replace_one_contact_among_many():
    """Тест замены номера у одного контакта среди нескольких"""
    data = {"Иван": "123-456", "Мария": "987-654", "Петр": "555-123"}
    result = add_contact_to_dict(data, "Иван", "000-000")
    assert result == {"Иван": "000-000", "Мария": "987-654", "Петр": "555-123"}
    assert "Иван" in result
    assert result["Иван"] == "000-000"