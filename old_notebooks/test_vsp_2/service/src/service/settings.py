from typing import TypeVar

from pydantic import field_validator, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

T = TypeVar("T")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_ignore_empty=False,  # required since OS does not allow empty env values on deployment
        extra="ignore",
        frozen=True,
        hide_input_in_errors=True,  # to avoid leaking secrets in error messages
        env_prefix="SERVICE_",  # to restrict the envs that get injected into the deployment
    )

    # required since OS does not allow non-string env values on deployment
    @field_validator("enable_cors", mode="before")
    def parse_enable_cors(cls, value: T) -> bool | T:
        if isinstance(value, str):
            cleaned_value = value.strip('"').lower()
            if cleaned_value == "true":
                return True
            elif cleaned_value == "false":
                return False
            else:
                raise ValueError(f'Invalid boolean string "{cleaned_value}"')
        return value

    enable_cors: bool = True
    pharia_kernel_address: HttpUrl
