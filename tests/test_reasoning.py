from nexus_lm.core.reasoning import REEREngine

def test_reer_initial_search():
    engine = REEREngine(max_iterations=1)
    trajectory = engine.search("Test Query")
    assert "<thought>" in trajectory
    assert "</thought>" in trajectory

def test_reer_mutations():
    engine = REEREngine(max_iterations=5)
    trajectory = engine.search("Complex Problem")
    assert trajectory.startswith("<thought>")
    assert trajectory.endswith("</thought>")

def test_reer_zero_iterations():
    engine = REEREngine(max_iterations=0)
    trajectory = engine.search("Test Query")
    assert trajectory == "<thought>\nLet me think... maybe we should address 'Test Query'.\n</thought>"
