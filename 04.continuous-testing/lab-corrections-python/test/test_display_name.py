import io

from src.user_functions import get_display_name_from_input


def test_d_name_input_too_short(monkeypatch):
    """Display name less than three chars"""
    u_name='a_lgaul'
    monkeypatch.setattr('sys.stdin', io.StringIO('a'))
    assert get_display_name_from_input(u_name) is None


def test_d_name_input_too_long(monkeypatch):
    """Display name greater than twenty chars"""
    u_name='a_lgaul'
    monkeypatch.setattr('sys.stdin', io.StringIO('Asterix' * 4))
    assert get_display_name_from_input(u_name) is None


def test_d_name_illegal_char(monkeypatch):
    """Display name illegal chars"""
    u_name='a_lgaul'
    monkeypatch.setattr('sys.stdin', io.StringIO('asterix!'))
    assert get_display_name_from_input(u_name) is None


def test_d_name_starts_with_non_letter(monkeypatch):
    """Display name illegal starting char"""
    u_name='a_lgaul'
    monkeypatch.setattr('sys.stdin', io.StringIO('42_asterix'))
    assert get_display_name_from_input(u_name) is None


def test_d_name_with_space(monkeypatch):
    """Test with space in d_name"""
    u_name='a_lgaul'
    monkeypatch.setattr('sys.stdin', io.StringIO('asterix the gaul'))
    assert get_display_name_from_input(u_name) is None


def test_d_name_valid(monkeypatch):
    """Test with valid d_name, char + _ + num"""
    u_name='a_lgaul'
    monkeypatch.setattr('sys.stdin', io.StringIO('asterix_42'))
    assert get_display_name_from_input(u_name) == 'asterix_42'


def test_d_name_fallback_on_empty_input(monkeypatch):
    """Test that an empty input defaults to u_name."""
    u_name = "algaul"
    monkeypatch.setattr("sys.stdin", io.StringIO("\n"))
    assert get_display_name_from_input(u_name) == u_name
