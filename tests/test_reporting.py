import pytest
from nexus_lm.reporting.bmc import BMCReportGenerator

def test_bmc_report_generation():
    generator = BMCReportGenerator(required_keywords=["cloud", "AI", "API"])
    data = "Our new AI product utilizes cloud infrastructure, accessible via API."
    trajectory = "<thought>The core features revolve around AI scalability.</thought>"

    report = generator.generate(data=data, trajectory=trajectory)

    assert report.hallucination_score == 4
    assert report.status == "Factually Sound"
    assert "AI" in report.customer_segments

def test_bmc_report_generation_no_trajectory():
    generator = BMCReportGenerator(required_keywords=["cloud", "AI", "API"])
    data = "Using AI and cloud through our new API."
    report = generator.generate(data=data)
    assert report.hallucination_score == 4
    assert report.status == "Factually Sound"
    assert report.customer_segments == data[:20]
