from os import environ
from typing import Dict

import pytest

from service.settings import Settings


@pytest.fixture
def env_variables() -> Dict[str, str]:
    return {
        "SERVICE_ENABLE_CORS": "False",
        "SERVICE_PHARIA_KERNEL_ADDRESS": "http://some-kernel-url.com/",
    }


@pytest.fixture
def set_env_variables(env_variables: Dict[str, str]) -> None:
    for key, value in env_variables.items():
        environ[key] = value


def test_loading_settings_succeeds_for_valid_values(
    env_variables: dict[str, str], set_env_variables: None
) -> None:
    settings = Settings()  # type: ignore

    for key, value in settings.model_dump().items():
        assert str(value) == env_variables[f"SERVICE_{key.upper()}"]


def test_loading_settings_raises_no_error_for_non_required_settings(
    set_env_variables: None,
) -> None:
    environ.clear()
    assert len(environ) == 0

    environ["SERVICE_PHARIA_KERNEL_ADDRESS"] = "http://some-kernel-url.com/"

    settings = Settings()  # type: ignore

    assert len(settings.model_dump()) > 0


@pytest.mark.parametrize(
    "env_variable, value",
    [
        ("SERVICE_ENABLE_CORS", "Fals"),
        ("SERVICE_PHARIA_KERNEL_ADDRESS", "www.some-kernel-url.com/"),
    ],
)
def test_settings_raises_an_error_for_an_invalid_setting(
    env_variable: str, value: str, set_env_variables: None
) -> None:
    environ[env_variable.upper()] = value

    with pytest.raises(Exception):
        Settings()  # type: ignore
