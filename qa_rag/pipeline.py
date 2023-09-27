import logging
from typing import List

import pydantic
from haystack import Pipeline
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import AnswerParser, PromptNode, PromptTemplate, TopPSampler
from haystack.nodes.ranker import LostInTheMiddleRanker
from haystack.nodes.retriever.web import WebRetriever
from haystack.nodes.translator import TransformersTranslator

from qa_rag.prompts import prompt_answer
from qa_rag.settings import settings


def get_prompt_node(prompt: str, settings: pydantic.BaseSettings) -> PromptNode:
    return PromptNode(
        model_name_or_path=settings.openai_model,
        default_prompt_template=PromptTemplate(prompt, output_parser=AnswerParser()),
        api_key=settings.openai_api_key,
        max_length=768,
        model_kwargs={"stream": True},
    )


def get_web_retriever(
    settings: pydantic.BaseSettings, allowed_domains: List[str]
) -> WebRetriever:
    return WebRetriever(
        api_key=settings.serper_api_key,
        allowed_domains=allowed_domains,
        top_search_results=10,
        mode="preprocessed_documents",
        top_k=50,
        cache_document_store=InMemoryDocumentStore(),
    )


def get_pipeline():
    pipeline = Pipeline()
    pipeline.add_node(
        component=get_web_retriever(
            settings=settings, allowed_domains=["stadt-koeln.de"]
        ),
        name="Retriever",
        inputs=["Query"],
    )
    pipeline.add_node(
        component=TopPSampler(top_p=0.90), name="Sampler", inputs=["Retriever"]
    )
    pipeline.add_node(
        component=LostInTheMiddleRanker(1024),
        name="LostInTheMiddleRanker",
        inputs=["Sampler"],
    )
    pipeline.add_node(
        component=get_prompt_node(prompt=prompt_answer, settings=settings),
        name="PromptNode",
        inputs=["LostInTheMiddleRanker"],
    )

    logging.disable(logging.CRITICAL)
    return pipeline
