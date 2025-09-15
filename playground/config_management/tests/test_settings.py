from app import application
from app.config.configuation import MySettings


def mock_get_settings():
    return MySettings(setting1=2, setting2="def")


def test_alt_setting(monkeypatch):
    monkeypatch.setattr(application, "get_settings", mock_get_settings)

    assert application.go() == 2


def test_old_settings(monkeypatch):
    assert application.go() == 1
