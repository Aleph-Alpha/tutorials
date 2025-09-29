from fastapi import APIRouter, Depends, HTTPException

from service.dependencies import get_token, with_kernel
from service.kernel import Json, Kernel, KernelException, Skill
from service.models import HealthResponse, QaInput

router: APIRouter = APIRouter()


@router.get("/health")
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.post("/qa")
async def qa(
    input: QaInput,
    token: str = Depends(get_token),
    kernel: Kernel = Depends(with_kernel),
) -> Json:
    skill = Skill(namespace="app", name="qa")
    try:
        response = await kernel.run(skill, token, input.model_dump())
        return response
    except KernelException as exp:
        error_message = ",".join(exp.args)
        if error_message.startswith(
            "Sorry, We could not find the skill you requested in its namespace"
        ):
            error_message += "\n\nPlease check https://docs.aleph-alpha.com/products/pharia-ai/pharia-studio/tutorial/pharia-applications-quick-start/#phariaai-application-skill for instructions on deploying the skill"
        print(error_message)
        raise HTTPException(exp.status_code, error_message) from exp
