from pharia_skill import ChatParams, Csi, IndexPath, Message, skill
from pydantic import BaseModel

NAMESPACE = "Studio"
COLLECTION = "papers"
INDEX = "asym-64"


class Input(BaseModel):
    question: str
    namespace: str = NAMESPACE
    collection: str = COLLECTION
    index: str = INDEX


class Output(BaseModel):
    answer: str | None
    sources: list[str] | None


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
    content = f"""Using the provided context documents below, answer the following question.
Format your response with the following sections: 
    1. SUMMARY: A brief 1-2 sentence answer to the question 
    2. DETAILS: A comprehensive explanation with specific information from the context 
    3. SOURCES: References to the specific parts of the context you used, if applicable If the information is not available in the context documents, clearly state this and provide a general response based on your knowledge, marked as [GENERAL KNOWLEDGE].

Input: {context}

Question: {input.question}
"""
    message = Message.user(content)
    params = ChatParams(max_tokens=512)
    response = csi.chat("llama-3.1-8b-instruct", [message], params)
    sources = [d.document_path.name for d in documents]
    return Output(answer=response.message.content, sources=sources)
