from src.utils import parse_command

def test_parse_command():
    # Тесты, которые у тебя уже есть
    assert parse_command('list "AsikSsort" +79210008832') == ('list', ('AsikSsort', '+79210008832'))
    assert parse_command('new "John Doe" 123456789') == ('new', ('John Doe', '123456789'))
    assert parse_command('list contacts phone') == ('list', ('contacts', 'phone'))
    assert parse_command('delete "Иван Иванов" 987654321') == ('delete', ('Иван Иванов', '987654321'))

def test_parse_command_exit():
    """Тест команды exit"""
    assert parse_command('exit') == ('exit', ('',))

def test_parse_command_with_spaces():
    """Тест с лишними пробелами"""
    assert parse_command('  list   "John  Doe"   +123  ') == ('list', ('John  Doe', '+123'))

def test_parse_command_empty_quotes():
    """Тест с пустыми кавычками"""
    try:
        parse_command('list "" +123')
        assert False, "Должно быть исключение"
    except Exception as e:
        assert str(e) == "неправильные аргументы"

def test_parse_command_multiple_words_no_quotes():
    """Тест с несколькими словами без кавычек"""
    try:
        parse_command('search john doe smith')
        assert False, "Должно быть исключение"
    except Exception as e:
        assert str(e) == "в команде слишком много аргументов"

def test_parse_command_single_argument():
    """Тест с одной командой и одним аргументом"""
    assert parse_command('help contacts') == ('help', ('contacts',))

def test_parse_command_special_characters():
    """Тест со специальными символами"""
    assert parse_command('new "O\'Connor" +1-234-567-8901') == ('new', ('O\'Connor', '+1-234-567-8901'))

def test_parse_command_not_enough_arguments():
    """Тест недостатка аргументов"""
    try:
        parse_command('list')
        assert False, "Должно быть исключение"
    except Exception as e:
        assert str(e) == "в команде недостает аргументов"

def test_parse_command_empty_command():
    """Тест пустой команды"""
    try:
        parse_command('')
        assert False, "Должно быть исключение"
    except Exception as e:
        assert str(e) == "в команде недостает аргументов"

def test_parse_command_only_spaces():
    """Тест команды из одних пробелов"""
    try:
        parse_command('   ')
        assert False, "Должно быть исключение"
    except Exception as e:
        assert str(e) == "в команде недостает аргументов"