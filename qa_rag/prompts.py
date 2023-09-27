prompt_answer = """
Synthesize a comprehensive answer from the provided paragraphs and the given question.\n
Focus on the question and avoid unnecessary information in your answer.\n
\n\n Paragraphs: {join(documents)} \n\n Question: {query} \n\n Answer:
"""


prompt_references = """
Create a concise and informative answer for a given question based solely on the given documents. You must only use information from the given documents.
Use an unbiased and journalistic tone. Do not repeat text. Avoid rephrasing. Cite the documents using Document[number] notation right after each sentence.
If the documents do not contain the answer to the question, say that ‘answering is not possible given the available information.’
{join(documents, delimiter=new_line, pattern=new_line+'Document[$idx]: $content', str_replace={new_line: ' ', '[': '(', ']': ')'})}

Question: {query};

Make sure you have citations after each sentence.
Answer: """
