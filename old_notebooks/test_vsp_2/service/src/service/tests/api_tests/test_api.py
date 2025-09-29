from http import HTTPStatus

from starlette.testclient import TestClient

from service.kernel import Skill
from service.models import HealthResponse

from .conftest import SaboteurKernel, SpyKernel


def test_get_health(
    test_client: TestClient,
) -> None:
    response = test_client.get("health")

    assert response.status_code == HTTPStatus.OK
    assert HealthResponse.model_validate_json(response.content) == HealthResponse(
        status="ok"
    )


def test_qa_invokes_kernel(client_and_spy: tuple[TestClient, SpyKernel]) -> None:
    # Given a app configured with a spy kernel
    client, spy = client_and_spy
    headers = {"Authorization": "Bearer token"}

    # When the QA route is called
    response = client.post("qa", json={"question": "A test question."}, headers=headers)

    # Then the spy kernel receives the token and data
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"answer": "A real answer."}
    assert len(spy.requests) == 1
    request = spy.requests[0]
    assert request.skill == Skill(namespace="app", name="qa")
    assert request.token == "token"
    assert request.data == {"question": "A test question."}


def test_qa_kernel_error_forwarded(
    client_and_saboteur: tuple[TestClient, SaboteurKernel],
) -> None:
    client, _ = client_and_saboteur
    headers = {"Authorization": "Bearer token"}

    # When the QA route is called
    response = client.post("qa", json={"question": "A test question."}, headers=headers)

    # Then the saboteur kernel raises
    assert response.status_code == 404


def test_response_without_body_does_not_crash(
    client_and_spy: tuple[TestClient, SpyKernel],
) -> None:
    # Given a client configured with a spy kernel
    client, _ = client_and_spy

    # When posting a request without a body
    response = client.post("qa", headers={"Authorization": "Bearer token"})

    # Then the response is a 422
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
