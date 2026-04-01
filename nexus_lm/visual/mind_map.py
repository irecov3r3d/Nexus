import re
from typing import List

from pydantic import BaseModel


class MindMapNode(BaseModel):
    """
    Visual map node structured for UI logic.
    """
    label: str
    children: List['MindMapNode'] = []

    # We allow recursive tree building
    model_config = {"arbitrary_types_allowed": True}


class MindMapEngine:
    """
    Visual Intelligence engine that extracts nodes directly from <thought> tags.
    """
    THOUGHT_PATTERN = re.compile(r"<thought>(.*?)</thought>", re.DOTALL)
    SPLIT_PATTERN = re.compile(r"[\n\.]+")

    def __init__(self, max_label_length: int = 50):
        self.max_label_length = max_label_length

    def extract_from_trajectory(self, trajectory: str) -> MindMapNode:
        """
        Parses reasoning trajectories into concise mind map nodes.
        Automatically truncates long reasoning lines to max_label_length.
        """
        root = MindMapNode(label="Root Problem")

        # Use re.finditer to find the last match more efficiently
        last_match = None
        for match in self.THOUGHT_PATTERN.finditer(trajectory):
            last_match = match

        if not last_match:
            return root

        # Simplistic parsing of reasoning steps separated by newline or period.
        thoughts = last_match.group(1).strip()
        parts = self.SPLIT_PATTERN.split(thoughts)

        for part in parts:
            part = part.strip()
            if not part:
                continue

            # Truncate visual node label
            if len(part) > self.max_label_length:
                part = part[:self.max_label_length - 3] + "..."

            root.children.append(MindMapNode(label=part))

        return root
