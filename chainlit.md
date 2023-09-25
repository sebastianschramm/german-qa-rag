# German QA rag pipeline with Haystack and chainlit

Navigating German Government Websites Made Easier

Finding specific information on German government websites can sometimes feel like quite a challenge. Whether it's permits, services, or valuable data you're after, the process can be a bit daunting.

Using deepset's Haystack, I've created a QA pipeline that incorporates translation models, SerperAPI, and GPT-3.5 to help you navigate the websites of the city of Cologne. With Haystack's WebRetriever, you can easily restrict Serper searches to specific domain names. Translation models (Helsinki-NLP) ensure your English queries are understood in German, and the GPT responses are seamlessly translated back into English.

This QA pipeline works in pure German as well, and I believe it can save you time in finding the information you need from the city hall in just a few seconds.

To make it even more user-friendly, I've added Chainlit for a conversational touch.
