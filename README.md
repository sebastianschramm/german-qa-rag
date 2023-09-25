# German QA rag pipeline with Haystack and chainlit

Navigating German Government Websites Made Easier

Finding specific information on German government websites can sometimes feel like quite a challenge. Whether it's permits, services, or valuable data you're after, the process can be a bit daunting.

Using deepset's Haystack, I've created a QA pipeline that incorporates translation models, SerperAPI, and GPT-3.5 to help you navigate the websites of the city of Cologne. With Haystack's WebRetriever, you can easily restrict Serper searches to specific domain names. Translation models (Helsinki-NLP) ensure your English queries are understood in German, and the GPT responses are seamlessly translated back into English.

This QA pipeline works in pure German as well, and I believe it can save you time in finding the information you need from the city hall in just a few seconds.

To make it even more user-friendly, I've added Chainlit for a conversational touch.

![Alt text](screenshot_qa.png?raw=true "QA example")

## Installation

You can install the qa_rag package via pip by executing the following command:

```bash
pip install git+https://github.com/sebastianschramm/german-qa-rag.git
```

or by first cloning the repository and then installing by executing the following command in the root of the cloned repository:

```bash
pip install .
```

## Start the app

You need to set the following environment variables before starting the app:

- SERPER_API_KEY (API key for using serper - free-tier accounts are available: https://serper.dev/signup)
- OPENAI_API_KEY (your API key for openai)
- OPENAI_MODEL (openai model name, e.g. "gpt-3.5-turbo")

You have 2 ways to start the QA app.
The recommended way is to use the provided script command "rag" (make sure you have the qa_rag package installed prior to that):

```bash
rag
```

Alternatively, if you have cloned the respository, you can use the chainlit cli in the root of the repository:

```bash
chainlit run qa_rag/server.py
```
