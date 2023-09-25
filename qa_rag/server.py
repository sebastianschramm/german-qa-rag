import chainlit as cl

from qa_rag.pipeline import get_pipeline

pipeline = get_pipeline()


@cl.on_message
async def main(message: str):
    response = await cl.make_async(pipeline.run)(message)
    await cl.Message(author="Haystack", content=response["answers"][0].answer).send()
