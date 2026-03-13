import sys
from pydantic import __version__ as pydantic_version
from typing import Dict, Any

from nexus_lm.core.ingestion import HierarchicalSemanticChunker, NodeExpansionLogic
from nexus_lm.core.reasoning import REEREngine
from nexus_lm.visual.mind_map import MindMapEngine
from nexus_lm.reporting.bmc import BMCReportGenerator
from nexus_lm.storage.metadata import MetadataStore
from nexus_lm.audio.tts_stack import AudioSynthesisStack

# ANSI escape sequences for coloring
C_RESET = "\033[0m"
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_MAGENTA = "\033[95m"

def print_header(title: str, color: str = C_CYAN):
    print(f"\n{color}{'=' * 60}")
    print(f" {title}")
    print(f"{'=' * 60}{C_RESET}")

def print_info(msg: str):
    print(f"{C_GREEN}[+] {msg}{C_RESET}")

def print_warn(msg: str):
    print(f"{C_YELLOW}[!] {msg}{C_RESET}")

def print_error(msg: str):
    print(f"{C_RED}[ERROR] {msg}{C_RESET}")

def print_mind_map(node, indent=""):
    print(f"{C_MAGENTA}{indent}└─ {node.label}{C_RESET}")
    for child in node.children:
        print_mind_map(child, indent + "    ")

def main():
    try:
        print_header("NexusLM: Advanced AI-First Knowledge OS", C_CYAN)
        print_info(f"Pydantic version: {pydantic_version}")

        # 1. Ingestion Phase
        print_header("Phase 1: Ingestion & Semantic Firewall", C_YELLOW)
        markdown_text = """
        # Enterprise AI Strategy
        NexusLM integrates AI RAG pipelines.
        ## The Cloud API Transition
        Moving to direct Cloud API access.
        """
        chunker = HierarchicalSemanticChunker()
        chunks = chunker.chunk(markdown_text)
        print_info(f"Generated {len(chunks)} structural chunks.")

        # 2. Reasoning Phase
        print_header("Phase 2: Deep Reasoning (REER Engine)", C_YELLOW)
        reasoning_engine = REEREngine(max_iterations=3)
        trajectory = reasoning_engine.search("How to adopt Enterprise AI through Cloud APIs?")
        print_info("Generated reasoning trajectory through PPL local search:")
        print(trajectory)

        # 3. Visual Mapping Phase
        print_header("Phase 3: Visual Intelligence Map", C_MAGENTA)
        mind_map_engine = MindMapEngine()
        root_node = mind_map_engine.extract_from_trajectory(trajectory)
        print_mind_map(root_node)

        # 4. Strategic Reporting Phase
        print_header("Phase 4: Strategic Reporting (BMC)", C_GREEN)
        report_generator = BMCReportGenerator(required_keywords=["cloud", "AI", "API"])

        # Combine chunks for grounding content
        combined_content = " ".join([c['content'] for c in chunks])
        report = report_generator.generate(data=combined_content, trajectory=trajectory)

        report_dict = report.model_dump()
        print_info(f"Generated Report Status: {report_dict['status']}")
        print_info(f"Hallucination Score: {report_dict['hallucination_score']}/4")

        # 5. Persistence Phase
        print_header("Phase 5: Local Data Sovereignty (Storage)", C_CYAN)
        store = MetadataStore()
        store.save_report(report_dict)
        latest = store.get_latest_report()
        if latest:
            print_info("Report successfully persisted to local SQLite database.")

        # 6. Audio Synthesis (Mock)
        print_header("Phase 6: Audio Synthesis", C_YELLOW)
        tts = AudioSynthesisStack("vibevoice")
        tts.initialize()
        audio = tts.synthesize("Synthesis complete.")
        print_info(f"Generated audio payload: {len(audio)} bytes")

        print_header("NexusLM Workflow Completed Successfully", C_GREEN)
        sys.exit(0)

    except Exception as e:
        print_error(f"Critical System Failure: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
