from typing import Literal

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["ok"]


class QaInput(BaseModel):
    question: str


class QaOutput(BaseModel):
    answer: str | None
