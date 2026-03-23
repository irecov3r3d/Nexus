from nexus_lm.core.ingestion import HierarchicalSemanticChunker, NodeExpansionLogic

def test_chunker_empty():
    chunker = HierarchicalSemanticChunker()
    chunks = chunker.chunk("")
    assert len(chunks) == 0

def test_chunker_markdown():
    chunker = HierarchicalSemanticChunker()
    text = "# Header 1\nContent 1\n## Header 2\nContent 2"
    chunks = chunker.chunk(text)
    assert len(chunks) == 2
    assert chunks[0]["level"] == 1
    assert chunks[0]["content"] == "Content 1"
    assert chunks[1]["level"] == 2
    assert chunks[1]["content"] == "Content 2"

def test_node_expansion_logic_basic():
    logic = NodeExpansionLogic()
    chunk = {"header": "Test Header", "content": "Test Content"}
    result = logic.expand(chunk)
    assert result == "Expanded: Test Header - Test Content"

def test_node_expansion_logic_missing_header():
    logic = NodeExpansionLogic()
    chunk = {"content": "Test Content"}
    result = logic.expand(chunk)
    assert result == "Expanded: Unknown - Test Content"

def test_node_expansion_logic_missing_content():
    logic = NodeExpansionLogic()
    chunk = {"header": "Test Header"}
    result = logic.expand(chunk)
    assert result == "Expanded: Test Header - "

def test_node_expansion_logic_empty():
    logic = NodeExpansionLogic()
    chunk = {}
    result = logic.expand(chunk)
    assert result == "Expanded: Unknown - "
