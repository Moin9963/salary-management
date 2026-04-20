from __future__ import annotations

from app.core.config import get_settings


def test_settings_use_local_defaults(monkeypatch) -> None:
    monkeypatch.delenv("APP_NAME", raising=False)
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("API_HOST", raising=False)
    monkeypatch.delenv("API_PORT", raising=False)
    get_settings.cache_clear()

    settings = get_settings()

    assert settings.app_name == "Employee Salary API"
    assert settings.environment == "development"
    assert settings.database_url == "sqlite:///./employee_salary.db"
    assert settings.api_host == "0.0.0.0"
    assert settings.api_port == 8000


def test_settings_can_be_overridden_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("APP_NAME", "Custom Employee API")
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./custom.db")
    monkeypatch.setenv("API_HOST", "127.0.0.1")
    monkeypatch.setenv("API_PORT", "9000")
    get_settings.cache_clear()

    settings = get_settings()

    assert settings.app_name == "Custom Employee API"
    assert settings.environment == "test"
    assert settings.database_url == "sqlite:///./custom.db"
    assert settings.api_host == "127.0.0.1"
    assert settings.api_port == 9000

    get_settings.cache_clear()
