# NexusLM: Advanced AI-First Knowledge Operating System

## Overview

NexusLM is a true "Knowledge Operating System," moving beyond standard retrieval toward a "deep reasoning" architecture. The primary differentiator is the REverse-Engineered Reasoning (REER) paradigm, treating reasoning as a gradient-free local search problem using perplexity (PPL).

## Features

- **Semantic Firewall:** Mitigates document-structure failures via Markdown-Aware Hierarchical Semantic Chunking.
- **REER Engine:** PPL-guided local search mutation strategy.
- **Visual Intelligence:** Dynamic mind maps extracted from reasoning trajectories.
- **Strategic Reporting:** 9-step Business Model Canvas (BMC) with dynamic factual grounding.
- **Multi-Modal Synthesis:** Audio synthesis capabilities (skeleton).
- **Data Sovereignty:** Local-first setup using SQLite for metadata persistence.

## Setup

1. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Knowledge OS Demo:
   ```bash
   PYTHONPATH=. python3 nexus_lm/main.py
   ```

3. Run the test suite:
   ```bash
   PYTHONPATH=. pytest tests/
   ```
