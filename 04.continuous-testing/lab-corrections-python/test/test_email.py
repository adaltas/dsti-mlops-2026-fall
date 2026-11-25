import io

from src.user_functions import get_email_from_input


def test_email_with_user_input_no_at_sign(monkeypatch):
    """Test no @"""
    email = "algaul.example.com"
    monkeypatch.setattr("sys.stdin", io.StringIO(email))
    assert get_email_from_input() is None


def test_email_with_user_input_no_dot(monkeypatch):
    """Test invalid TLD"""
    email = "algaul@examplecom"
    monkeypatch.setattr("sys.stdin", io.StringIO(email))
    assert get_email_from_input() is None


def test_email_with_user_input_correct(monkeypatch):
    """Test valid"""
    email = "algaul@example.com"
    monkeypatch.setattr("sys.stdin", io.StringIO(email))
    assert get_email_from_input() == email
