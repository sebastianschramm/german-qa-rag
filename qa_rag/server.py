import chainlit as cl

from qa_rag.pipeline import get_pipeline
from qa_rag.verify import validate_citations

pipeline = get_pipeline()


@cl.on_message
async def main(message: str):
    response = await cl.make_async(pipeline.run)(message)
    source_urls = {
        f"Document[{j}]": (doc.meta["url"], doc.content)
        for j, doc in enumerate(response["invocation_context"]["documents"], start=1)
    }
    answer = await validate_citations(response["answers"][0].answer, source_urls)
    await cl.Message(author="Haystack", content=f"{answer}").send()
    for key, value in source_urls.items():
        url, content = value
        await cl.Text(
            name=key,
            content=f"SOURCE_URL:\n{url}\n\nSOURCE_SNIPPET:\n{content}",
            display="side",
        ).send()
