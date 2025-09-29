import pytest
from pharia_skill.testing import StubCsi
from pharia_skill import (
    SearchResult,
    DocumentPath,
    Message,
    ChatParams,
    ChatResponse,
    Role,
    FinishReason,
    TokenUsage,
    SearchFilter,
    Cursor,
)

from qa import IndexPath, Input, custom_rag


class CustomStubCsi(StubCsi):
    def search(
        self,
        index_path: IndexPath,
        query: str,
        max_results: int = 1,
        min_score: float | None = None,
        filters: list[SearchFilter] | None = None,
    ) -> list[SearchResult]:
        if "Heidelberg" in query:
            return []
        return [
            SearchResult(
                document_path=DocumentPath(
                    namespace=index_path.namespace,
                    collection=index_path.collection,
                    name="article1.txt",
                ),
                content="The first law states that human dignity shall be inviolable.",
                score=0.95,
                start=Cursor(item=1, position=0),
                end=Cursor(item=2, position=1),
            )
        ]

    def chat(
        self, model: str, messages: list[Message], params: ChatParams
    ) -> ChatResponse:
        return ChatResponse(
            message=Message(
                role=Role.Assistant,
                content="Das erste Gesetz besagt, dass die Würde des Menschen unantastbar ist.",
            ),
            finish_reason=FinishReason.STOP,
            logprobs=[],
            usage=TokenUsage(prompt=0, completion=0),
        )


@pytest.fixture
def csi() -> StubCsi:
    return CustomStubCsi()


@pytest.fixture
def index() -> IndexPath:
    return IndexPath(
        namespace="Assistant",
        collection="Grundgesetz",
        index="luminousBase-64-0-asymmetric-semantic",
    )


def test_custom_rag_out_of_document_bound(csi: StubCsi, index: IndexPath):
    input = Input(
        question="How many people live in Heidelberg?",
        namespace=index.namespace,
        collection=index.collection,
        index=index.index,
    )
    result = custom_rag(csi, input)
    assert result.answer is None


def test_custom_rag_within_document_bound(csi: StubCsi, index: IndexPath):
    input = Input(
        question="Was ist das erste Gesetz?",
        namespace=index.namespace,
        collection=index.collection,
        index=index.index,
    )
    result = custom_rag(csi, input)
    assert result.answer
    assert "Gesetz" in result.answer
