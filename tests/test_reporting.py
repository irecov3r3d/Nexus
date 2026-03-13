from nexus_lm.reporting.bmc import BMCReportGenerator, BMCReport

def test_bmc_report_initialization():
    report = BMCReport()
    assert report.hallucination_score == 0
    assert report.status == "Disqualified"

def test_bmc_factual_grounding():
    generator = BMCReportGenerator(required_keywords=["cloud", "AI", "enterprise", "RAG"])
    assert generator._calculate_factual_grounding("Using cloud") == 2
    assert generator._calculate_factual_grounding("Using cloud for enterprise AI apps") == 4
    assert generator._calculate_factual_grounding("Nothing useful here.") == 1

def test_bmc_report_generation():
    generator = BMCReportGenerator(required_keywords=["cloud", "AI", "API"])
    data = "Using AI and cloud through our new API."
    report = generator.generate(data=data, trajectory="Reasoning path")
    assert report.hallucination_score == 4
    assert report.status == "Factually Sound"
    assert "AI" in report.customer_segments
