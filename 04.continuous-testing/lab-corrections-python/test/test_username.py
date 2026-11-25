import io

from src.user_functions import get_user_name_from_input


def test_username_with_input_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a lgaul'))
    assert get_user_name_from_input() is None

def test_username_with_input_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
    assert get_user_name_from_input() is None

def test_username_with_input_correct_1(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('algaul'))
    assert get_user_name_from_input() == 'algaul'

def test_username_with_input_correct_2(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Algaul'))
    assert get_user_name_from_input() == 'Algaul'
