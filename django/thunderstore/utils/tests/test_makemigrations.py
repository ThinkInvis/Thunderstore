import pytest

from thunderstore.utils.makemigrations import StubStorage, is_makemigrations_check


def test_utils_stub_storage():
    storage = StubStorage()
    with pytest.raises(NotImplementedError):
        storage.save("test", b"test")


def test_utils_is_makemigrations_check_true(mocker):
    mocker.patch("sys.argv", ["manage.py", "makemigrations"])
    assert is_makemigrations_check() is True


def test_utils_is_makemigrations_check_false(mocker):
    mocker.patch("sys.argv", ["manage.py", "runserver"])
    assert is_makemigrations_check() is False
