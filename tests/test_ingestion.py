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
