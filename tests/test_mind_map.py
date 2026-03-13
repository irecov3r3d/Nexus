from nexus_lm.visual.mind_map import MindMapEngine, MindMapNode

def test_mind_map_empty():
    engine = MindMapEngine()
    node = engine.extract_from_trajectory("")
    assert node.label == "Root Problem"
    assert len(node.children) == 0

def test_mind_map_extraction():
    engine = MindMapEngine(max_label_length=50)
    traj = "<thought>\nFirst idea.\nSecond idea is very long and should be truncated properly.\n</thought>"
    node = engine.extract_from_trajectory(traj)
    assert len(node.children) == 2
    assert node.children[0].label == "First idea"
    assert "..." in node.children[1].label
    assert len(node.children[1].label) <= 50
