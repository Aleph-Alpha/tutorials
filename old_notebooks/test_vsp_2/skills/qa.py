from pharia_skill import ChatParams, Csi, IndexPath, Message, skill
from pydantic import BaseModel

NAMESPACE = "Studio"
COLLECTION = "pharia-tutorial-rag-vsp-1"
INDEX = "rag-tutorial-index-1"


class Input(BaseModel):
    question: str
    namespace: str = NAMESPACE
    collection: str = COLLECTION
    index: str = INDEX


class Output(BaseModel):
    answer: str | None


@skill
def custom_rag(csi: Csi, input: Input) -> Output:
    index = IndexPath(
        namespace=input.namespace,
        collection=input.collection,
        index=input.index,
    )

    if not (documents := csi.search(index, input.question, 3, 0.5)):
        return Output(answer=None)

    context = "\n".join([d.content for d in documents])
    content = f"""Using the provided context documents below, answer the following question accurately and comprehensively. If the information is directly available in the context documents, cite it clearly. If not, use your knowledge to fill in the gaps while ensuring that the response is consistent with the given information. Do not fabricate facts or make assumptions beyond what the context or your knowledge base provides. Ensure that the response is structured, concise, and tailored to the specific question being asked.

Input: {context}

Question: {input.question}
"""
    message = Message.user(content)
    params = ChatParams(max_tokens=512)
    response = csi.chat("llama-3.1-8b-instruct", [message], params)
    return Output(answer=response.message.content)
