import os
from functools import lru_cache

from fastapi import Header, HTTPException, Request

from service.kernel import Kernel
from service.settings import Settings


@lru_cache
def with_settings() -> Settings:
    from dotenv import load_dotenv

    load_dotenv(verbose=True)

    # mypy complains about missing named arguments (required attributes without a default)
    loaded_settings = Settings()  # type: ignore
    print(loaded_settings)  # TODO: use logger
    return loaded_settings


def get_token(authorization: str = Header(...)) -> str:
    # this enables to run the service locally during development
    if authorization.startswith("Bearer "):
        return authorization[len("Bearer ") :]
    elif (token := os.environ.get("PHARIA_AI_TOKEN")) is not None:
        return token
    raise HTTPException(status_code=400, detail="Invalid authorization header")


def with_kernel(request: Request) -> Kernel:
    return request.state.kernel
