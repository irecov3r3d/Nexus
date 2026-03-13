import re
from typing import List, Dict, Any

class HierarchicalSemanticChunker:
    """
    Implements a Markdown-Aware Semantic Firewall to mitigate Mapped Failure Modes,
    specifically No. 5 (Embedding Drift) and No. 8 (Traceability Failure).
    """
    def __init__(self):
        # Matches markdown headers (e.g., # Header, ## Subheader)
        # We need robustness against leading spaces and missing newlines.
        self.header_pattern = re.compile(r'^\s*(#{1,6})\s+(.+)$', re.MULTILINE)

    def chunk(self, text: str) -> List[Dict[str, Any]]:
        if not text.strip():
            return []

        chunks = []
        # Find all headers
        matches = list(self.header_pattern.finditer(text))

        if not matches:
            # No headers, return single chunk
            return [{"header": "Root", "content": text.strip()}]

        # If there's content before the first header
        if matches[0].start() > 0:
            pre_content = text[:matches[0].start()].strip()
            if pre_content:
                chunks.append({"header": "Root", "content": pre_content})

        for i, match in enumerate(matches):
            header_level = len(match.group(1))
            header_text = match.group(2).strip()

            start_pos = match.end()
            end_pos = matches[i+1].start() if i + 1 < len(matches) else len(text)

            content = text[start_pos:end_pos].strip()
            chunks.append({
                "header": header_text,
                "level": header_level,
                "content": content
            })

        return chunks


class NodeExpansionLogic:
    """
    Expands nodes initialized with a global plan via the semantic firewall.
    """
    def expand(self, chunk: Dict[str, Any]) -> str:
        # A simple placeholder expansion
        return f"Expanded: {chunk.get('header', 'Unknown')} - {chunk.get('content', '')}"
