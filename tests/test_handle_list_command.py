import pytest
from commands.list import handle_list_command


# Тестовые данные
@pytest.fixture
def sample_data():
    return {
        "Alice": "123-456",
        "Bob": "789-012",
        "Charlie": "345-678"
    }


def test_handle_list_command_all_contacts(sample_data):
    """Тест: вывод всех контактов"""
    result = handle_list_command(sample_data, None)

    assert 'Все контакты:' in result
    assert '1. Alice' in result
    assert '2. Bob' in result
    assert '3. Charlie' in result


def test_handle_list_command_empty_data():
    """Тест: вывод контактов при пустых данных"""
    result = handle_list_command({})
    assert result == 'Контактов нет'


def test_handle_list_command_specific_contact_found(sample_data):
    """Тест: вывод конкретного контакта (найден)"""
    result = handle_list_command(sample_data, ("Alice",))
    assert result == "Alice: 123-456"


def test_handle_list_command_specific_contact_not_found(sample_data):
    """Тест: вывод конкретного контакта (не найден)"""
    result = handle_list_command(sample_data, ("NonExistent",))
    assert result == 'Такого контакта не существует'


def test_handle_list_command_empty_tuple(sample_data):
    """Тест: пустой tuple параметров"""
    result = handle_list_command(sample_data, ())
    assert 'Все контакты:' in result


def test_handle_list_command_multiple_params(sample_data):
    """Тест: несколько параметров в tuple (берется только первый)"""
    result = handle_list_command(sample_data, ("Alice", "Bob", "Charlie"))
    assert result == "Alice: 123-456"


def test_handle_list_command_single_element_tuple():
    """Тест: tuple с одним элементом"""
    test_data = {"Single": "123"}
    result = handle_list_command(test_data, ("Single",))
    assert result == "Single: 123"


def test_handle_list_command_none_params():
    """Тест: None вместо tuple"""
    test_data = {"Test": "123"}
    result = handle_list_command(test_data)
    assert 'Все контакты:' in result
    assert '1. Test' in result


def test_handle_list_command_case_sensitive(sample_data):
    """Тест: регистрозависимость поиска"""
    result = handle_list_command(sample_data, ("alice",))  # lowercase
    assert result == 'Такого контакта не существует'


def test_handle_list_command_special_characters():
    """Тест: контакт с пробелами и специальными символами"""
    test_data = {
        "John Smith": "123-456",
        "Анна-Мария": "789-012"
    }

    result1 = handle_list_command(test_data, ("John Smith",))
    assert result1 == "John Smith: 123-456"

    result2 = handle_list_command(test_data, ("Анна-Мария",))
    assert result2 == "Анна-Мария: 789-012"


def test_handle_list_command_single_contact():
    """Тест: один контакт в списке"""
    test_data = {"Single": "123"}
    result = handle_list_command(test_data)
    assert result == 'Все контакты:\n1. Single'


# Параметризованные тесты
@pytest.mark.parametrize("test_data,params,expected", [
    ({}, None, 'Контактов нет'),
    ({"Test": "123"}, None, 'Все контакты:\n1. Test'),
    ({"Test": "123"}, ("Test",), "Test: 123"),
    ({"Test": "123"}, ("NotFound",), 'Такого контакта не существует'),
])
def test_handle_list_command_parametrized(test_data, params, expected):
    """Параметризованный тест для основных сценариев"""
    result = handle_list_command(test_data, params)
    if expected in ['Контактов нет', 'Такого контакта не существует'] or ':' in expected:
        assert result == expected
    else:
        assert expected in result