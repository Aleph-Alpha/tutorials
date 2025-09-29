import os

import pytest
from dotenv import load_dotenv

from service.kernel import HttpKernel, KernelException, Skill

PHARIA_KERNEL_ADDRESS = "SERVICE_PHARIA_KERNEL_ADDRESS"
PHARIA_AI_TOKEN = "PHARIA_AI_TOKEN"


async def test_http_kernel_runs_skill() -> None:
    load_dotenv()
    token = os.environ[PHARIA_AI_TOKEN]
    kernel = HttpKernel(url=os.environ[PHARIA_KERNEL_ADDRESS])
    skill = Skill(namespace="playground", name="haiku")
    input = {"topic": "Oat milk"}
    response = await kernel.run(skill, token, input)
    assert "creamy" in str(response).lower()


async def test_kernel_exception() -> None:
    load_dotenv()
    token = "bad token"
    kernel = HttpKernel(url=os.environ[PHARIA_KERNEL_ADDRESS])
    skill = Skill(namespace="non_existing", name="non_existing")
    input = {"bad_input": "dummy"}
    with pytest.raises(KernelException):
        await kernel.run(skill, token, input)
