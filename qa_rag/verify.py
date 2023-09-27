import re
from typing import List

pattern = re.compile(r"\(Document\[\d+\]\)")


async def validate_citations(text: str, sources: List[str]):
    matches = re.findall(pattern, text)
    invalid_matches = [match for match in matches if match not in sources]
    for invalid_citation in invalid_matches:
        text = text.replace(invalid_citation, "")
    return text
