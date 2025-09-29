from typing import Any, Iterable, Mapping, NamedTuple, Sequence

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from service.dependencies import with_kernel
from service.kernel import Json, Kernel, KernelException, Skill
from service.main import app


@fixture()
def fast_api() -> FastAPI:
    return app


@fixture()
def test_client(fast_api: FastAPI) -> TestClient:
    return TestClient(app=fast_api)


class ModelTestClient(TestClient):
    def models(self) -> Sequence[Mapping[str, Any]]:
        return []


@fixture()
def model_test_client(fast_api: FastAPI) -> Iterable[TestClient]:
    with ModelTestClient(fast_api) as client:
        yield client


class Request(NamedTuple):
    skill: Skill
    token: str
    data: Json


class SpyKernel(Kernel):
    def __init__(self) -> None:
        self.requests: list[Request] = []

    async def run(self, skill: Skill, token: str, input: Json) -> Json:
        self.requests.append(Request(skill, token, input))
        return {"answer": "A real answer."}


class SaboteurKernel(Kernel):
    async def run(self, skill: Skill, token: str, input: Json) -> Json:
        raise KernelException(404, "should never run")


@fixture()
def client_and_spy(
    fast_api: FastAPI,
) -> Iterable[tuple[TestClient, SpyKernel]]:
    kernel = SpyKernel()
    fast_api.dependency_overrides[with_kernel] = lambda: kernel
    client = TestClient(fast_api)
    yield client, kernel
    fast_api.dependency_overrides = {}


@fixture()
def client_and_saboteur(
    fast_api: FastAPI,
) -> Iterable[tuple[TestClient, SaboteurKernel]]:
    kernel = SaboteurKernel()
    fast_api.dependency_overrides[with_kernel] = lambda: kernel
    client = TestClient(fast_api)
    yield client, kernel
    fast_api.dependency_overrides = {}
