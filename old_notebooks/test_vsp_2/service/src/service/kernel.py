from typing import NamedTuple, Protocol

import httpx
from httpx import Timeout

Json = dict | list | bool | float | int | str | None


class Skill(NamedTuple):
    namespace: str
    name: str

    def as_str(self) -> str:
        return f"{self.namespace}/{self.name}"


class KernelException(Exception):
    def __init__(self, status_code: int, msg: str):
        self.status_code = status_code
        super().__init__(msg)


class Kernel(Protocol):
    async def run(self, skill: Skill, token: str, input: Json) -> Json: ...


class HttpKernel(Kernel):
    """Execute skills in the Kernel.

    Cache connections to the Kernel across skill executions.
    """

    def __init__(self, url: str) -> None:
        self.url = url
        timeout = Timeout(read=120, connect=10, write=10, pool=10)
        self.session = httpx.AsyncClient(timeout=timeout)

    async def run(self, skill: Skill, token: str, input: Json) -> Json:
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{self.url}v1/skills/{skill.namespace}/{skill.name}/run"
        response = await self.session.post(url, json=input, headers=headers)
        if response.status_code >= 400:
            raise KernelException(response.status_code, response.text)
        return response.json()

    async def shutdown(self):
        await self.session.aclose()
