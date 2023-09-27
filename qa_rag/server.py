import chainlit as cl

from qa_rag.pipeline import get_pipeline

pipeline = get_pipeline()


@cl.on_message
async def main(message: str):
    response = await cl.make_async(pipeline.run)(message)
    source_urls = "\n".join(set([doc.meta['url'] for doc in response['invocation_context']['documents']]))
    await cl.Message(author="Haystack", content=f"{response['answers'][0].answer}").send()
    await cl.Message(author="HaystackContextReferencer", content=f"{source_urls}").send()
