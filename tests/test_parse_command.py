from src.utils import parse_command

def test_parse_command():
    assert parse_command('list "AsikSsort" +79210008832') == ('list', ('AsikSsort', '+79210008832'))

