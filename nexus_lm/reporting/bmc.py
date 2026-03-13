from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class BMCReport(BaseModel):
    """
    9-Step Business Model Canvas structured report.
    """
    customer_segments: str = "Unidentified"
    value_propositions: str = "Unidentified"
    channels: str = "Unidentified"
    customer_relationships: str = "Unidentified"
    revenue_streams: str = "Unidentified"
    key_resources: str = "Unidentified"
    key_activities: str = "Unidentified"
    key_partnerships: str = "Unidentified"
    cost_structure: str = "Unidentified"
    hallucination_score: int = Field(default=0, ge=0, le=4)
    status: str = "Disqualified"

class BMCReportGenerator:
    """
    Generates strategic intelligence reports and implements Keyword-Based Factual Grounding.
    """
    def __init__(self, required_keywords: List[str] = ["cloud", "AI", "enterprise", "API", "RAG"]):
        self.required_keywords = required_keywords

    def _calculate_factual_grounding(self, content: str) -> int:
        """
        Dynamically calculates hallucination severity score (0 to 4).
        Score 4 is Factually Sound, < 4 triggers warnings/disqualification.
        """
        if not content:
            return 0

        content_lower = content.lower()
        found_count = sum(1 for keyword in self.required_keywords if keyword.lower() in content_lower)

        # Simple heuristic mapping for the 4-point severity scale
        if found_count >= 3:
            return 4
        elif found_count == 2:
            return 3
        elif found_count == 1:
            return 2
        else:
            return 1

    def generate(self, data: str, trajectory: Optional[str] = None) -> BMCReport:
        score = self._calculate_factual_grounding(data)
        status = "Factually Sound" if score == 4 else "Disqualified (Critical Hallucination)"

        # A mock synthesis logic using reasoning and data
        synthesis = f"{data} | {trajectory}" if trajectory else data

        return BMCReport(
            customer_segments=synthesis[:20],
            value_propositions="Deep Reasoning AI",
            channels="Direct API Sales",
            customer_relationships="Automated Lifecycle",
            revenue_streams="SaaS Model",
            key_resources="Proprietary RAG Engines",
            key_activities="Model Tuning",
            key_partnerships="Cloud Providers",
            cost_structure="Compute Inference Costs",
            hallucination_score=score,
            status=status
        )
